from rest_framework import serializers
from armory.models.cabinet import Cabinet

class CabinetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cabinet
        fields = "__all__"
