from rest_framework import serializers
from .models import CallbacksTeste, TokensTeste

class CallbacksTesteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallbacksTeste
        fields = '__all__'

    
class TokensTesteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TokensTeste
        fields = '__all__'