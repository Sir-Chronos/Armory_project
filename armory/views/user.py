from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from armory.models.user import User
from armory.serializers.user import UserSerializer

class UserView(APIView):

    def get(self, request, id=None):

        if id is not None:
            try:
                user = User.objects.get(pk=id)  # Tenta encontrar o user pelo ID
                serializer = UserSerializer(user, many=False)
                return Response(serializer.data)
        
            except User.DoesNotExist:
                return Response({'detail': 'User não encontrado'}, status=status.HTTP_404_NOT_FOUND)

        else:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        try:
            user = User.objects.get(pk=id)  # Tenta encontrar o user pelo ID
        except User.DoesNotExist:
            return Response({'detail': 'User não encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserSerializer(user, data=request.data)  # Passa o user encontrado e os dados da requisição para o serializer
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        try:
            user = User.objects.get(pk=id)  # Tenta encontrar o user pelo ID
        except User.DoesNotExist:
            return Response({'detail': 'User não encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        user.delete()  # Exclui o user encontrado
        return Response({'detail': 'User excluído com sucesso'}, status=status.HTTP_204_NO_CONTENT)