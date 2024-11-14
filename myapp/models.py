from django.db import models

class MediaItens(models.Model):
    MEDIA_TYPES = [
        ('movie','Movie'),
        ('series','Series'),
        ('anime', 'Anime'),
    ]

    name = models.CharField(max_length=255)
    type = models.CharField(max_length=15, choices=MEDIA_TYPES)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    register = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__() -> str:
        return self.name
    
