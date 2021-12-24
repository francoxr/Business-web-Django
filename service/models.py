from django.db import models

# Create your models here.
class Service(models.Model):

    title = models.CharField(max_length=200, verbose_name='Titulo')
    subtitle = models.CharField(max_length=200, verbose_name='Subtitulo')
    content = models.TextField(blank=True, verbose_name='Contenido')
    image = models.ImageField(verbose_name='Imagen', upload_to="services")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')

    class Meta:
        """Se agregan metadatos extendidos"""
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
        ordering = ["created_at"]
    
    def __str__(self):
        return self.title