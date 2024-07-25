from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Nosotros(models.Model):
    image = models.ImageField(verbose_name='Imagen', upload_to='nosotros')
    name = models.CharField(verbose_name='Nombre', max_length=200)
    puesto = models.CharField(verbose_name='Especialidad', max_length=100)
    trayectoria = RichTextField(verbose_name='Trayectoria')

    class Meta:
        verbose_name ='nosotros'
        verbose_name_plural = 'Nosotros'
        ordering = ['-name']

    def __str__(self):
        return self.name
    

