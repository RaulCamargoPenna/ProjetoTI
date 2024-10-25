# Projeto do Setor de TI da empresa:

Ferramentas utilizadas:
- Django;
- Django Rest Framework;
- Channels;
- Celery;
- Redis;
- Flowbite (CND apaenas para desenvolvimento);
- Tailwind CSS (CND apaenas para desenvolvimento);
- Flower (ainda não inlcuído);

  A ideia aqui é ter um painel de monitoramento da aplicação, como possuimos filas de processamento, tokens e outras informações
  que precisamos monitorar essa página será atualizada em tempo real utilizando Consumers e WebSockets.

  Irei utilizar signals para fazer no post save, a chamada de um função Celery que irá chamar o Consumer para fazer as analises das tabelas que precisam ser monitoradas e como não quero causar lentidão
  na aplicação esperando o singals emitir o sinal e o Consumer terminar sua tarefa, vou usar o CELERY para fazer uma tarefa assíncrona.

#### Métricas que serão analisadas:
- Contagem de callbacks não processados: O consumer irá filtrar a tabela dos callbacks para ver quantos ainda não foram processados, no página eu defini algumas quantidades que indicarão normalidade na fila, lentidão ou alerta de possível erro;
- Tempo de expiração de token: O consumer irá devolver para cada token, qual foi a data e hora da última atualização, como alguns deles expiram dentro de algumas hora, irei disponibilizar no front a validade do token;
- Flower: Haverá um botão para redirecionar o usuário para o flower, onde ele poderá aconpanhar o status das filas e das tasks executadas;

## Abaixo um ilustração do fluxo:
  ![Fluxo dados em tempo real websocket + celery](https://github.com/user-attachments/assets/a7885c27-20dd-46ae-88bd-74ebbf553904)



## Para utilizar:
- pip install -r requirements.txt
- python manage.py migrate

**Em outro terminal (necessário ter o serviço do redis rodando)**:
- celery -A app worker -Q fila_rapida --pool=solo -l info 

Caso esteja usando Windows será necessário usar o WSL para dar start no serviço do redis, siga os passos do link abaixo:
https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/install-redis-on-windows/

Para realizar testes entrei na página que tem as métris e utilizei o Postman e fiz alguns posts nas tabelas criadas, você irá notas a atualização da métrica de callbacks e a atualização da barra abaixo.
**Projeto em andamento, atualizações irão entrar semanalmente.**

