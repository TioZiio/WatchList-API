from rest_framework import serializers
from .models import MediaItens

class MediaItensSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaItens
        fields = '__all__'
