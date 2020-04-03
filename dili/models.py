from django.db import models
from django.utils import timezone



class Ben(models.Model):
    baslik = models.CharField(max_length=200)
    icerik = models.TextField()
    yayinlanma_zamanı = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def __str__(self):
        return self.title