from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
import json
from .models import CallbacksTeste, TokensTeste
from django.db.models import F

class ConsumerMetricas(AsyncWebsocketConsumer):
    """
        Consumer teste para enviar mensagens via websockets. A ideia aqui vai ser
        construir um painel para o setor de T.I para monitorar callbacks, informações
        dos tokens, etc.
    """

    async def connect(self):
        """
            Método de conexão, ao se conectar cria um 'canal' chamado métricas
            aceita a conexão e envia os dados de contagem.
        """
        await self.channel_layer.group_add("metricas", self.channel_name)
        await self.accept()
        await self.send_info()  # Envia a contagem inicial quando conecta

    async def disconnect(self, code):
        """
            Método disconnect, fecha a conexão e remove o grupo criado.
        """
        await self.channel_layer.group_discard("metricas", self.channel_name)

    async def receive(self, text_data=None, bytes_data=None):
        """
            Método com capacidade de receber informações do client. 
            Ficará em standby
        """
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        sender = text_data_json['sender']
        
        await self.send(text_data=json.dumps({
            'message': message,
            'sender': sender
        }))

    async def send_info(self):
        """ 
            Método que irá enviar a contagem.
        """
        count = await self.get_count_callback()  # Chamada assíncrona para buscar a contagem
        tokens = await self.get_info_token()
        await self.send(text_data=json.dumps({
                'callbacks_count': count,
                'tokens_info': tokens
            }))

    @sync_to_async
    def get_count_callback(self):
        """
            Método que faz a contagem
        """
        return CallbacksTeste.objects.filter(processado=False).count()  # Operação síncrona

    @sync_to_async
    def get_info_token(self):
        tokens = TokensTeste.objects.values('id', 'token').annotate(ultima_att = F('ultima_atualizacao'))
        info_tokens = {item['id']: {'nome': item['token'], 'ult_att': item['ultima_att'].strftime("%d/%m/%Y %H:%M:%S")} for item in tokens}

        return info_tokens

    async def update_count(self, event):
        """
            Método que será chamado pelo signals toda vez que um item do Callbackteste
            for criado ou atualizado
        """
        # Este método será chamado pelo grupo ao receber o evento "send_info"
        await self.send_info()