from django.shortcuts import render, redirect
from aplicacionFirma.models import *
from aplicacionFirma.forms import *

# Create your views here.

def home(request):
	
	if request.method=='POST':
		form=InicioForm(request.POST, request.FILES)
		
		if form.is_valid():
			datos=form.cleaned_data
			dni =datos['dni']
			nombre=datos['nombre']
			apellido1=datos['apellido1']
			apellido2=datos['apellido2']
			texto=datos['formulario']

			nuevo=Usuario(dni=dni,nombre=nombre, apellido1=apellido2, apellido2=apellido2)
			nuevo.save()
			
			Formulario.objects.create(texto='texto', usuario=nuevo)
			return redirect('Datos')
	else: 

		form=InicioForm()

	return render (request,"home.html",{"form":form})

def datos(request):

	if request.method=='POST':
		form=InicioForm(request.POST)
		print (request.POST)
		if form.is_valid():
			datos=form.cleaned_data
			dni =datos['dni']
			nombre=datos['nombre']
			apellido1=datos['apellido1']
			apellido2=datos['apellido2']
			texto=datos['formulario']
			nuevo=Usuario(dni='dni',nombre='nombre', apellido1='apellido2', apellido2='apellido2')
			nuevo.save()
			formulario=Formulario(texto='texto', usuario='nuevo')

	
	return render(request,"datos.html")