from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from django.http import JsonResponse
from rest_framework import generics
from .models import CallbacksTeste, TokensTeste 
from .serializers import CallbacksTesteSerializer, TokensTesteSerializer

# Create your views here.
class Index(TemplateView):
    template_name = 'base.html'


class CallbackTesteCreateListView(generics.ListCreateAPIView):
    queryset = CallbacksTeste.objects.all()
    serializer_class = CallbacksTesteSerializer

class CallbackTesteCreateRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = CallbacksTeste.objects.all()
    serializer_class = CallbacksTesteSerializer


class TokensTesteCreateListView(generics.ListCreateAPIView):
    queryset = TokensTeste.objects.all()
    serializer_class = TokensTesteSerializer

class TokensTesteCreateRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = TokensTeste.objects.all()
    serializer_class = TokensTesteSerializer

from .tasks import send_info_to_websocket
class Teste(View):

    def get(self, request):
        send_info_to_websocket.delay() 
    
        return JsonResponse({'teste': 'sucesso'})