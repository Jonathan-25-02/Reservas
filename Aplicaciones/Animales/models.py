

# Create your models here.
# models.py
from django.db import models

class ReservaNatural(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.TextField()

    def __str__(self):
        return self.nombre

class Animal(models.Model):
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=100)
    edad_aproximada = models.IntegerField()
    fecha_rescate = models.DateField()
    foto = models.ImageField(upload_to='animales/', blank=True, null=True)


    def __str__(self):
        return self.nombre

class EventoLiberacion(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    reserva = models.ForeignKey(ReservaNatural, on_delete=models.CASCADE)
    fecha_liberacion = models.DateField()
    observaciones = models.TextField(blank=True)
    documento = models.FileField(upload_to='eventos/', blank=True, null=True)


    def __str__(self):
        return f"{self.animal} en {self.reserva}"
