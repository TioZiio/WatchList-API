from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal

class MediaItens(models.Model):
    class Meta:
        verbose_name = 'Catálogo'
        verbose_name_plural = 'Catálogo'
        db_table = 'media_itens'

    MEDIA_TYPES = [
        ('movie','Movie'),
        ('series','Series'),
        ('anime', 'Anime'),
    ]

    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=MEDIA_TYPES)
    rating = models.DecimalField(
        max_digits=3, 
        decimal_places=1,
        validators=[MinValueValidator(Decimal('0.0')),
                    MaxValueValidator(Decimal('10.0'))])
    
    # Register
    register_date = models.DateField(auto_now_add=True)
    register_time = models.TimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.name} ({self.gender}) - Nota: {self.rating}"
    
