from django.urls import path
from . import views
from .views import login_view 

urlpatterns = [
    path('', views.inicio, name='login'),
    # ...
    path('login/', login_view, name='login'),



    # Animales
    path('animales/', views.animales, name='animales'),
    path('nuevoAnimal/', views.nuevoAnimal),
    path('guardarAnimal/', views.guardarAnimal),
    path('eliminarAnimal/<int:id>/', views.eliminarAnimal),
    path('editarAnimal/<int:id>/', views.editarAnimal),
    path('procesarEdicionAnimal/<int:id>/', views.procesarEdicionAnimal),

    # Reservas
    path('reservas/', views.reservas, name='reservas'),
    path('nuevaReservaNatural/', views.nuevaReserva),
    path('guardarReservaNatural/', views.guardarReserva),
    path('eliminarReservaNatural/<int:id>/', views.eliminarReserva),
    path('editarReservaNatural/<int:id>/', views.editarReserva),
    path('procesarEdicionReservaNatural/<int:id>/', views.procesarEdicionReserva),

    # Eventos
    path('eventos/', views.eventos, name='eventos'),
    path('nuevoEventoLiberacion/', views.nuevoEvento),
    path('guardarEventoLiberacion/', views.guardarEvento),
    path('eliminarEventoLiberacion/<int:id>/', views.eliminarEvento),
    path('editarEventoLiberacion/<int:id>/', views.editarEvento),
    path('procesarEdicionEventoLiberacion/<int:id>/', views.procesarEdicionEvento),
]
