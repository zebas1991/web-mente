from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['-created']


    def __str__(self):
        return self.name
    

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Título')
    content = RichTextField(verbose_name='Contenido')
    published = models.DateTimeField(verbose_name='Fecha de publicación', default=now)
    image = models.ImageField(verbose_name='Imagen', upload_to='blog', null=True, blank=True)
    author = models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name='Categorías', related_name='get_posts')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'
        ordering = ['-created']

    def __str__(self):
        return self.title
    
    @property
    def image_url(self):
        if self.image:
            return self.image.url
        return ''  # Retorna una cadena vacía si no hay imagen
    
    


