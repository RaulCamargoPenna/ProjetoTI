from django.urls import path
from .views import Index, CallbackTesteCreateListView, CallbackTesteCreateRetrieveUpdateDestroy, TokensTesteCreateListView, TokensTesteCreateRetrieveUpdateDestroy, Teste

app_name = 'setor_ti'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('callback', CallbackTesteCreateListView.as_view(), name='list_create_callback'),
    path('callback/<int:pk>', CallbackTesteCreateRetrieveUpdateDestroy.as_view(), name='details_callback'),
    path('token', TokensTesteCreateListView.as_view(), name='list_create_token'),
    path('token/<int:pk>', TokensTesteCreateRetrieveUpdateDestroy.as_view(), name='details_token'),
    path('teste', Teste.as_view(), name='Teste')
]