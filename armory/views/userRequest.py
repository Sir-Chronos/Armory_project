from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from armory.models.user import User
from armory.models.log import Log
from armory.models.cabinet import Cabinet

from armory.serializers.user import UserSerializer
from armory.serializers.cabinet import CabinetSerializer
from armory.serializers.log import LogSerializer

class UserRequestView(APIView):

    def get(self, request, token, cabinet):
        try:
            user = User.objects.get(telegram_token=token)
            user_serializer = UserSerializer(user)
        except User.DoesNotExist:
            return Response({"Error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        try:
            cabinet = Cabinet.objects.get(pk=cabinet)
            cabinet_serializer = CabinetSerializer(cabinet)
        except Cabinet.DoesNotExist:
            return Response({"Error": "Cabinet not found"}, status=status.HTTP_404_NOT_FOUND)
        
        # Crie uma instância de Log com os dados relevantes
        log_data = {
            'user': user.pk,
            'cabinet': cabinet.pk,
        }
        log_serializer = LogSerializer(data=log_data)
        if log_serializer.is_valid():
            log_serializer.save()
        else:
            return Response({"Error": "Failed to create log"}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"user": True, "cabinet": True})

