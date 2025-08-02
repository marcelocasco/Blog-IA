from django.contrib import admin
from .models import Categoria,Noticia,Comentario

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display=('titulo','contenido','fecha_emision', 'autor','categoria')
    list_filter=('fecha_emision', 'categoria')
    search_fields=('titulo','contenido')

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display=('nombre',)
    
@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'noticia', 'fecha')
    list_filter = ('fecha',)
    search_fields = ('contenido',)
    
#admin.site.register(Noticia,NoticiaAdmin):     esto se cambia por @admin.register()