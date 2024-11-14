from django.contrib import admin
from .models import MediaItens

@admin.register(MediaItens)
class InsertItens(admin.ModelAdmin):
    list_display = 'id', 'name', 'rating', 'type',

