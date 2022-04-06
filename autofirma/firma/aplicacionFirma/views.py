from django.shortcuts import render, redirect
from aplicacionFirma.models import *

# Create your views here.

def home(request):

	return render (request,"home.html")
