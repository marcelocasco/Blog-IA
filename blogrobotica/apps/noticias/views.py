from django.shortcuts import render, redirect, get_object_or_404,redirect
from .models import Noticia
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import NoticiaForm, PerfilForm,RegistroUsuarioForm


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
    if request.method=='POST': #pregunta si va a crear el formulario (pregunta por POST)
        form=NoticiaForm(request.POST) #cargo el formulacio, con el aspecto ya guardado de los models
        if form.is_valid(): #pregunta si es valido el formulario
            noticia=form.save(commit=False)#evita el autoguardado
            noticia.autor=request.user #carga el usuario actual
            noticia.save() #guarda la noticia
            return redirect('lista_noticias') 
    else:
        form = NoticiaForm() #muestra formulario en blanco en caso de no completar
    contexto={'form':form}
    return render(request, 'crear.html', contexto)
        

@login_required    
def editar_noticia(request,id_ing):
    render(request,'editar.html')

@login_required
def eliminar_noticia(request):
    render(request,'eliminar.html')

@login_required
def crear_perfil(request):
    try:
        perfil=request.user.perfil #verifica si existe el perfil
        return redirect('lading')
    except perfil.DoesNotExist:
        if request.method=='POST': #pregunta si va a crear el formulario (pregunta por POST)
            form=PerfilForm(request.POST) #cargo el formulacio, con el aspecto ya guardado de los models
            if form.is_valid(): #pregunta si es valido el formulario
                perfil=form.save(commit=False)#evita el autoguardado
                perfil.usuario=request.user #carga el usuario actual
                perfil.save() #guarda el perfil
                return redirect('landing') 
        else:
            form = PerfilForm() #muestra formulario en blanco en caso de no completar
    contexto={'form':form}
    return render(request, 'crear_perfil.html', contexto)
    
def registrar_usuario(request):
    if request.method=='POST':
        form=RegistroUsuarioForm(request.POST)
        if form.is_valid():
            usuario=form.save()
            login(request, usuario)
            return redirect('crear_perfil')
    else:
        form=RegistroUsuarioForm()
    contexto={'form':form}
    return render(request,'registrar_usuario.html', contexto)

