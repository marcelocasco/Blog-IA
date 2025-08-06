from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Categoria(models.Model):
    nombre=models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre

class Noticia(models.Model):
    titulo=models.CharField(max_length=100)
    contenido=models.TextField()
    fecha_emision=models.DateTimeField(auto_now_add=True)
    autor=models.ForeignKey(User,on_delete=models.CASCADE)
    categoria=models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    noticia=models.ForeignKey(Noticia, on_delete=models.CASCADE, related_name='comentarios')
    usuario=models.ForeignKey(User,on_delete=models.CASCADE)
    contenido=models.TextField()
    fecha=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.usuario.username}-{self.noticia.titulo}'
    
class Perfil(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    bio=models.TextField(null=True, blank=True)
    avatar=models.ImageField(upload_to=True, blank=True, null=True)

    def __str__(self):
        return f'Perfil de {self.user.username}'    
    
    
    