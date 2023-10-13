from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from armory.models.cabinet import Cabinet
from armory.serializers.cabinet import CabinetSerializer

class CabinetView(APIView):

    def get(self, request, id=None):

        if id is not None:
            try:
                cabinet = Cabinet.objects.get(pk=id)  # Tenta encontrar o cabinet pelo ID
                serializer = CabinetSerializer(cabinet, many=False)
                return Response(serializer.data)
        
            except Cabinet.DoesNotExist:
                return Response({'detail': 'Cabinet não encontrado'}, status=status.HTTP_404_NOT_FOUND)

        else:
            cabinets = Cabinet.objects.all()
            serializer = CabinetSerializer(cabinets, many=True)
            return Response(serializer.data)
    
    def post(self, request):
        serializer = CabinetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        try:
            cabinet = Cabinet.objects.get(pk=id)  # Tenta encontrar o cabinet pelo ID
        except Cabinet.DoesNotExist:
            return Response({'detail': 'Cabinet não encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CabinetSerializer(cabinet, data=request.data)  # Passa o cabinet encontrado e os dados da requisição para o serializer
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        try:
            cabinet = Cabinet.objects.get(pk=id)  # Tenta encontrar o cabinet pelo ID
        except Cabinet.DoesNotExist:
            return Response({'detail': 'Cabinet não encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        cabinet.delete()  # Exclui o cabinet encontrado
        return Response({'detail': 'Cabinet excluído com sucesso'}, status=status.HTTP_204_NO_CONTENT)