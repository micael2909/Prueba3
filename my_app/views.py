from django.shortcuts import render
from .models import Vehiculo
from .forms import FormularioVehiculo

def index(request):
	return render(request,'my_app/index.html',{})

def vendedor(request):
    vehiculo = Vehiculo()
    
    if request.method == 'POST':
        nuevo_vehiculo = FormularioVehiculo(request.POST, instance=vehiculo)
        nuevo_vehiculo.save()
        return render(request, 'my_app/index.html', {})
    else:
        formulario = FormularioVehiculo()
        return render(request, 'my_app/vendedor.html', {'formulario': formulario})