from django.shortcuts import render, get_object_or_404,redirect
from .models import Noticia
from django.contrib.auth.decorators import login_required


# Create your views here.
def landing(request):
    return render(request,'landing.html')

def sobre_nosotros(request):
    return render(request, 'sobre_nosotros.html')

def lista_noticias(request):
    noticias=Noticia.objects.all().order_by('fecha_emision')
    contexto={'noticias':noticias} #este noticias es que el html va a usar como referencia
    return render(request, 'lista.html', contexto)

def detalle_noticia(request,id_ing):
    noticia=get_object_or_404(Noticia,id=id_ing)
    contexto={'noticia':noticia}
    return render(request, 'detalle.html',contexto)

@login_required
def crear_noticia(request):
    render(request, 'noticia/crear.html')
    
@login_required    
def editar_noticia(request,id_ing):
    render(request,'editar.html')

@login_required
def eliminar_noticia(request):
    render(request,'eliminar.html')


    