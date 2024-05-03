from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    titulo = models.CharField(max_length=30)
    subtitulo = models.CharField(max_length=30)
    cuerpo = models.CharField(max_length=1000)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateField()
    imagen = models.ImageField()
    def __str__(self):
        return f"Titulo: {self.titulo} - Subtitulo: {self.subtitulo} - Autor: {self.autor} - Imagen: {self.imagen}"
    
class Message(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=30)
    def __str__(self):
        return f"Usuario: {self.username} - Mensaje: {self.message}"
    
class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)
    def __str__(self):
        return f"{self.user} - {self.imagen}"