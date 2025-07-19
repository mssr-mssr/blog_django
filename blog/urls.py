from django.urls import path
from . import views

urlpatterns = [
    path('', views.iniciar_sesion, name = 'login'),
    path('posts/', views.lista_posts, name='lista_posts'),
    path('post/<int:pk>/', views.detalle_post, name='detalle_post'),
    path('crear/', views.crear_post, name='crear_post'),
    path('registro/', views.registro, name='registro'),
    path('login/',views.iniciar_sesion, name='login'),
    path('logout/', views.cerrar_sesion, name='logout'),
]