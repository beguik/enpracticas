from django.urls import path
from aplicacionFirma import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns =[ 
	path('', views.home, name="Inicio"),
	path('formulario/', views.formulario, name="Formulario"),
	#path('datos', views.datos, name="Datos"),
	path('pdf/<int:id>', views.exportarPdf, name="Pdf"),
]



urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)