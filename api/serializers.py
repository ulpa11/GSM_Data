from rest_framework import serializers
from .models import GSM

class GSMSerializer(serializers.ModelSerializer):
    class Meta:
        model=GSM
        fields="__all__"
