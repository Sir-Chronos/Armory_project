from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from armory.models.log import Log
from armory.serializers.log import LogSerializer

class LogView(APIView):

    def get(self, request, id=None):

        if id is not None:
            try:
                log = Log.objects.get(pk=id)  # Tenta encontrar o log pelo ID
                serializer = LogSerializer(log, many=False)
                return Response(serializer.data)
        
            except Log.DoesNotExist:
                return Response({'detail': 'Log não encontrado'}, status=status.HTTP_404_NOT_FOUND)

        else:
            logs = Log.objects.all()
            serializer = LogSerializer(logs, many=True)
            return Response(serializer.data)
    
    def post(self, request):
        serializer = LogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)