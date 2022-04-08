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
			if validarDni(dni):
				nuevo=Usuario(dni=dni,nombre=nombre, apellido1=apellido2, apellido2=apellido2)
				nuevo.save()
				Formulario.objects.create(texto=texto, usuario=nuevo)
				usuario=Usuario.objects.get(dni=dni)
				contador=Formulario.objects.count()
				formularios=Formulario.objects.get(id_formulario=contador)
			
				#borrador=Formulario.objects.order_by('id_formulario').last()
				#form=Formulario.objects.get(id_formulario=borrador)
				print(usuario)
				print('pasa')
			
				
				return render(request,'datos.html',{'usuario':usuario, 'contador':contador, 'formularios':formularios})
			else: 
				
				return redirect('Formulario')
	else:

		form=InicioForm()

	return render (request,"home.html",{"form":form}, )


def formulario(request):
	
	if request.method=='POST':
		form=InicioForm(request.POST, request.FILES)
		
		if form.is_valid():
			datos=form.cleaned_data
			dni =datos['dni']
			nombre=datos['nombre']
			apellido1=datos['apellido1']
			apellido2=datos['apellido2']
			texto=datos['formulario']
			if validarDni(dni):
				nuevo=Usuario(dni=dni,nombre=nombre, apellido1=apellido2, apellido2=apellido2)
				nuevo.save()
				Formulario.objects.create(texto='texto', usuario=nuevo)
				usuario=Usuario.objects.get(dni=dni)
				print(usuario)
				print('pasa')
				return render(request,'datos.html',{'usuario':usuario})
			else: 
				
				return redirect('Formulario')
	else:

		form=InicioForm()


	return render(request,"formulario.html",{"form":form},)


def datos(request):
	




	return render(request,"datos.html")






def validarDni(dni):
	if len(dni)==9:
		numeros=int(dni[0:8])
		letra=dni[8:].upper()
		modulo=numeros%23
		clave="TRWAGMYFPDXBNJZSQVHLCKET"
		cl=clave[modulo:modulo+1]
		if(letra!=cl):
			return False
			print("hola1")
		else:
			return True
			print("hola2")





