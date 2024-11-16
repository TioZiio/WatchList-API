from rest_framework import viewsets
from .models import MediaItens
from .serializers import MediaItensSerializer
from django.shortcuts import render
from django.http import JsonResponse

class MediaItensViewSet(viewsets.ModelViewSet):

    queryset = MediaItens.objects.all()
    serializer_class = MediaItensSerializer

def index(request):
    print(request.POST)
    if request.method == 'POST':
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        rating = request.POST.get('rating')

        if not name:
            return JsonResponse({'error': 'Nome é Obrigatório'}, status=400)
        try:
            rating = float(rating)
            if rating < 0 or rating > 10:
                return JsonResponse({'error': 'Nota deve estar entre 0 e 10'}, status=400)
        except ValueError:
            return JsonResponse({'error': 'Valor inválido inserido'}, status=400)

        MediaItens.objects.create(name=name, gender=gender, rating=rating)

        return JsonResponse({'message': 'Item adicionado com sucesso!'})

    return render(
        request,
        'global/index.html',
    )
