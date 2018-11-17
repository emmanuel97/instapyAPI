from chaves.models import Chave
from chaves.serializers import ChaveSerializer
from rest_framework import generics,status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response

class ListarChave(generics.ListCreateAPIView):# faz operacoes get e post sobre uma lista de chaves
    queryset = Chave.objects.all()
    serializer_class = ChaveSerializer

class ValidarChave(APIView):
    """
    Retrieve, update or delete a chave instance.
    """
    def get_object(self, chave):
        try:
            print(chave)
            return Chave.objects.get(chave=chave)
        except Chave.DoesNotExist:
            raise Http404

    def get(self, request, chave, format=None):
        key = self.get_object(chave)
        serializer = ChaveSerializer(key)
        return Response(serializer.data)
    #
    # def put(self, request, pk, format=None):
    #     snippet = self.get_object(pk)
    #     serializer = SnippetSerializer(snippet, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # def delete(self, request, pk, format=None):
    #     snippet = self.get_object(pk)
    #     snippet.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)



class DetalharChave(generics.RetrieveUpdateDestroyAPIView):#faz operacoes get, delete e put uma chave
    queryset = Chave.objects.all()
    serializer_class = ChaveSerializer
