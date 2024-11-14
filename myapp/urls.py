from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MediaItensViewSet

app_name = 'myapp'

router = DefaultRouter()
router.register(r'catalogo', MediaItensViewSet)

urlpatterns = [
    path('', include(router.urls), name='catalogo'),
]
