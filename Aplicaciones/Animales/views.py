from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Animal, ReservaNatural, EventoLiberacion
# views.py
from django.contrib.auth import authenticate, login as auth_login

def login_view(request):
    if request.method == 'POST':
        usuario = request.POST['username']
        clave = request.POST['password']
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            auth_login(request, user)
            return redirect('animales')  # o donde quieras redirigir
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'login.html')

# INICIO - Página principal del sistema
@login_required
def inicio(request):
    return render(request, "login.html")

# ANIMAL
@login_required
def animales(request):
    lista = Animal.objects.all()
    return render(request, "animal.html", {'animales': lista})

@login_required
def nuevoAnimal(request):
    return render(request, "nuevoAnimal.html")

@login_required
def guardarAnimal(request):
    nombre = request.POST["nombre"]
    especie = request.POST["especie"]
    edad = request.POST["edad_aproximada"]
    fecha = request.POST["fecha_rescate"]
    foto = request.FILES.get("foto")  # obteniendo imagen

    Animal.objects.create(
        nombre=nombre,
        especie=especie,
        edad_aproximada=edad,
        fecha_rescate=fecha,
        foto=foto
    )
    messages.success(request, "Animal guardado exitosamente")
    return redirect('/animales/')

@login_required
def eliminarAnimal(request, id):
    animal = get_object_or_404(Animal, id=id)
    animal.delete()
    return redirect('/animales/')

@login_required
def editarAnimal(request, id):
    animal = get_object_or_404(Animal, id=id)
    return render(request, "editarAnimal.html", {'animal': animal})

@login_required
def procesarEdicionAnimal(request, id):
    animal = get_object_or_404(Animal, id=id)
    animal.nombre = request.POST["nombre"]
    animal.especie = request.POST["especie"]
    animal.edad_aproximada = request.POST["edad_aproximada"]
    animal.fecha_rescate = request.POST["fecha_rescate"]
    foto_nueva = request.FILES.get("foto")

    if foto_nueva:
        animal.foto = foto_nueva  # reemplaza si hay nueva imagen

    animal.save()
    messages.success(request, "Animal actualizado exitosamente")
    return redirect('/animales/')

# RESERVA NATURAL
@login_required
def reservas(request):
    lista = ReservaNatural.objects.all()
    return render(request, "reservaNatural.html", {'reservas': lista})

@login_required
def nuevaReserva(request):
    return render(request, "nuevaReservaNatural.html")

@login_required
def guardarReserva(request):
    nombre = request.POST["nombre"]
    ubicacion = request.POST["ubicacion"]
    ReservaNatural.objects.create(nombre=nombre, ubicacion=ubicacion)
    messages.success(request, "Reserva guardada exitosamente")
    return redirect('/reservas/')

@login_required
def eliminarReserva(request, id):
    reserva = get_object_or_404(ReservaNatural, id=id)
    reserva.delete()
    return redirect('/reservas/')

@login_required
def editarReserva(request, id):
    reserva = get_object_or_404(ReservaNatural, id=id)
    return render(request, "editarReservaNatural.html", {'reserva': reserva})

@login_required
def procesarEdicionReserva(request, id):
    reserva = get_object_or_404(ReservaNatural, id=id)
    reserva.nombre = request.POST["nombre"]
    reserva.ubicacion = request.POST["ubicacion"]
    reserva.save()
    messages.success(request, "Reserva actualizada exitosamente")
    return redirect('/reservas/')

# EVENTO DE LIBERACIÓN
# EVENTOS DE LIBERACIÓN
@login_required
def eventos(request):
    lista = EventoLiberacion.objects.all()
    return render(request, "eventoLiberacion.html", {'eventos': lista})

@login_required
def nuevoEvento(request):
    animales = Animal.objects.all()
    reservas = ReservaNatural.objects.all()
    return render(request, "nuevoEventoLiberacion.html", {'animales': animales, 'reservas': reservas})

@login_required
def guardarEvento(request):
    animal_id = request.POST["animal"]
    reserva_id = request.POST["reserva"]
    fecha = request.POST["fecha_liberacion"]
    observaciones = request.POST["observaciones"]
    documento = request.FILES.get("documento")  # PDF u otro archivo

    EventoLiberacion.objects.create(
        animal_id=animal_id,
        reserva_id=reserva_id,
        fecha_liberacion=fecha,
        observaciones=observaciones,
        documento=documento
    )
    messages.success(request, "Evento de liberación guardado exitosamente")
    return redirect('/eventos/')

@login_required
def eliminarEvento(request, id):
    evento = get_object_or_404(EventoLiberacion, id=id)
    evento.delete()
    return redirect('/eventos/')

@login_required
def editarEvento(request, id):
    evento = get_object_or_404(EventoLiberacion, id=id)
    animales = Animal.objects.all()
    reservas = ReservaNatural.objects.all()
    return render(request, "editarEventoLiberacion.html", {
        'evento': evento,
        'animales': animales,
        'reservas': reservas
    })

@login_required
def procesarEdicionEvento(request, id):
    evento = get_object_or_404(EventoLiberacion, id=id)
    evento.animal_id = request.POST["animal"]
    evento.reserva_id = request.POST["reserva"]
    evento.fecha_liberacion = request.POST["fecha_liberacion"]
    evento.observaciones = request.POST["observaciones"]
    archivo_nuevo = request.FILES.get("documento")

    if archivo_nuevo:
        evento.documento = archivo_nuevo  # reemplaza el archivo si hay uno nuevo

    evento.save()
    messages.success(request, "Evento actualizado exitosamente")
    return redirect('/eventos/')

