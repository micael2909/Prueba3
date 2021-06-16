from django import forms
from .models import Vehiculo

class FormularioVehiculo(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ('VIN', 'Patente', 'Año_Fabricacion', 'Fecha_de_Recepcion', 'Marca', 'Modelo',)

        widgets={
            'VIN': forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese identificador del vehiculo'}),
            'Patente': forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese la Patente del Vehiculo'}),
            'Año_Fabricacion': forms.NumberInput(attrs={'class':'form-control','placeholder':'Ingrese Año fabricacion de Vehiculo ej: 2016','type':'number'}),
            'Fecha_de_Recepcion': forms.DateInput(attrs={'class':'form-control','type':'date','placeholder':'Ingrese Fecha de Recepcion del vehiculo'}),
            'Marca': forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese Marca del Vehiculo'}),
            'Modelo': forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese Modelo del Vehiculo'}),
        }