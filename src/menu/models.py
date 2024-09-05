from django.db import models
from plat.models import Plat

# Create your models here.

class Menu(models.Model):
    plat = models.OneToOneField('plat.Plat', on_delete=models.CASCADE)
    creation_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"Menu du {self.creation_date}"
        
class Meta:
    verbose_name = 'Menu'
    verbose_name_plural = 'Menus'