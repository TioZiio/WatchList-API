from django.conf.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MediaItensList

router = DefaultRouter()
router.register(r'catalogo', MediaItensList)

urlpatterns = [
    path('', include(router.urls), name='catalogo'),
]
