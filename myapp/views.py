from rest_framework import viewsets
from .models import MediaItens
from .serializers import MediaItensSerializer
from django.shortcuts import render

class MediaItensViewSet(viewsets.ModelViewSet):

    queryset = MediaItens.objects.all()
    serializer_class = MediaItensSerializer

def index(request):
    return render(
        request,
        'global/index.html',
    )
