from django.db import models
from django.utils import timezone

class Vehiculo(models.Model):
	VIN = models.CharField(max_length=17,primary_key=True)
	Patente = models.CharField(max_length=6)
	Año_Fabricacion = models.PositiveIntegerField()
	Fecha_de_Recepcion = models.DateTimeField()
	Marca = models.CharField(max_length=200)
	Modelo = models.CharField(max_length=200)

	def publish(self):
		self.save()

	def __str__(self):
		return self.VIN