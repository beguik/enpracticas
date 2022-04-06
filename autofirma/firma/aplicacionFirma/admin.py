from django.contrib import admin
from aplicacionFirma.models import *

class UsuarioAdmin(admin.ModelAdmin):
	readonly_fields:('created','updated')
	search_fields=("apellido1",)

class FormularioAdmin(admin.ModelAdmin):
	readonly_fields:('created',)
	search_fields=("id_formulario",)
	list_filter=("usuario",)

class BorradorAdmin(admin.ModelAdmin):
	readonly_fields:('created',)
	search_fields=("id_borrador",)


class ProgramaFirmaAdmin(admin.ModelAdmin):
	readonly_fields:('created',)
	search_fields=("nombre",)

class ArchivoFirmadoAdmin(admin.ModelAdmin):
	readonly_fields:('created',)
	search_fields=("id_archivo",)






admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Formulario, FormularioAdmin)
admin.site.register(Borrador, BorradorAdmin)
admin.site.register(ProgramaFirma, ProgramaFirmaAdmin)
admin.site.register(ArchivoFirmado, ArchivoFirmadoAdmin)


# Register your models here.
