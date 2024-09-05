from django.db import models

# Create your models here.
class Plat(models.Model):
    name = models.CharField(max_length=200)
    summary = models.TextField()

    def __str__(self):
        return self.name
        
class Meta:
    verbose_name = 'Plat'
    verbose_name_plural = 'Plats'