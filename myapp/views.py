from rest_framework import generics
from .models import MediaItens
from .serializers import MediaItensSerializer

class MediaItensList(generics.ListCreateAPIView):

    queryset = MediaItens.objects.all()
    serializer_class = MediaItensSerializer

