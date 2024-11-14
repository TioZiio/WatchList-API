from rest_framework import viewsets
from .models import MediaItens
from .serializers import MediaItensSerializer

class MediaItensViewSet(viewsets.ModelViewSet):

    queryset = MediaItens.objects.all()
    serializer_class = MediaItensSerializer

