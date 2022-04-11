from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
from weasyprint.text.fonts import FontConfiguration
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
#Mas adelante habrá que filtrar dni para que no se registren dni con diferentes atributos y se machaquen los datos
#primero preguntar a Emilio cual es el proceso. 
				nuevo=Usuario(dni=dni,nombre=nombre, apellido1=apellido1, apellido2=apellido2)
				nuevo.save()
				Formulario.objects.create(texto=texto, usuario=nuevo)
				usuario=Usuario.objects.get(dni=dni)
				formularios=Formulario.objects.latest('id_formulario')
				return render(request,'datos.html',{'usuario':usuario, 'formularios':formularios})
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
				Formulario.objects.create(texto=texto, usuario=nuevo)
				usuario=Usuario.objects.get(dni=dni)
				formularios=Formulario.objects.latest('id_formulario')			
				return render(request,'datos.html',{'usuario':usuario, 'formularios':formularios})
			else: 
				
				return redirect('Formulario')
	else:

		form=InicioForm()


	return render(request,"formulario.html",{"form":form},)


def exportarPdf(request,id):

	formularios=Formulario.objects.get(id_formulario=id)
	usuario=Usuario.objects.get(dni=formularios.usuario_id)	


	contexto={'formularios':formularios, 'usuario':usuario}
	html=render_to_string('archivo_pdf.html',contexto)
	response=HttpResponse(content_type="application/pdf")
	response["Content-Disposition"]="inline; archivo.pdf"

	font_config=FontConfiguration()
	HTML(string=html, base_url=request.build_absolute_uri()).write_pdf(response, font_config=font_config)
	return response


def confirmar(request, id):

	formularios=Formulario.objects.get(id_formulario=id)
	usuario=Usuario.objects.get(dni=formularios.usuario_id)	

	return render(request,"confirmar.html",{"formularios":formularios, "usuario":usuario},)

def eliminar(request, id):
	formulario=Formulario.objects.get(id_formulario=id)
	usuario=Usuario.objects.get(dni=formulario.usuario_id)
	print('prueba')
	if request.method=="POST":
		print('entra')
		formulario.delete()
		return redirect('Inicio')

	return render(request, "eliminar.html", {"formulario":formulario,"usuario":usuario})


def validarDni(dni):
	if len(dni)==9:
		numeros=int(dni[0:8])
		letra=dni[8:].upper()
		modulo=numeros%23
		clave="TRWAGMYFPDXBNJZSQVHLCKET"
		cl=clave[modulo:modulo+1]
		if(letra!=cl):
			return False
		else:
			return True
			





