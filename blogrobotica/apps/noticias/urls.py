from django.urls import path
from .import views

urlpatterns=[
    path('',views.landing, name='landing'), 
    path('sobre_nosotros/', views.sobre_nosotros,name='sobre_nosotros'),
    path('noticia/', views.lista_noticias,name='lista_noticias'),
    path('noticia/<int:id_ing>/', views.detalle_noticia,name='detalle_noticia'),
    path('noticia/crear/', views.crear_noticia,name='crear_noticia'),
    path('noticia/<int:id_ing>/editar/', views.editar_noticia,name='editar_noticia'), 
    path('noticia/<int:id_ing>/eliminar/', views.eliminar_noticia,name='eliminar_noticia'),
    path('perfil/crear/', views.crear_perfil, name='crear_perfil'),
    path('registro/', views.registrar_usuario, name='registrar_usuario'), 

]