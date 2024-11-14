from django.db import models

class MediaItens(models.Model):
    class Meta:
        verbose_name = 'Catálogo'
        verbose_name_plural = 'Catálogo'

    MEDIA_TYPES = [
        ('movie','Movie'),
        ('series','Series'),
        ('anime', 'Anime'),
    ]

    name = models.CharField(max_length=255)
    type = models.CharField(max_length=15, choices=MEDIA_TYPES)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    
    # Register
    register_date = models.DateField(auto_now_add=True)
    register_time = models.TimeField(auto_now_add=True)
    # Update
    update_date = models.DateField(auto_now=True)
    update_time = models.TimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
    
