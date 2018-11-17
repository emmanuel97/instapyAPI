from rest_framework import serializers
from chaves.models import Chave


class ChaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chave
        fields = ('id', 'chave', 'dono', 'senha')
