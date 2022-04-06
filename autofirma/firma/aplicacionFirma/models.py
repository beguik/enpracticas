from django.db import models

class Usuario (models.Model):
	dni = models.CharField(max_length= 9,primary_key=True)
	nombre = models.CharField(max_length=20)
	apellido1 = models.CharField(max_length=20)
	apellido2 = models.CharField(max_length=20)
	certificado = models.CharField(max_length=600, null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True, null=True)
	updated = models.DateTimeField(auto_now_add=True, null=True)

	class Meta:
		verbose_name='usuario'
		verbose_name_plural = 'usuarios'

	def __str__(self):

		cadena=self.nombre+" , "+self.apellido1+" "+self.apellido2
		return cadena.capitalize()


class Formulario (models.Model):
	id_formulario= models.AutoField(primary_key=True)
	texto = models.CharField(max_length=512)
	usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True, null=True)

	class Meta:
		verbose_name='formulario'
		verbose_name_plural='formularios'

	def __str__(self):
		return str(self.id_formulario)


class Borrador (models.Model):
	id_borrador = models.AutoField(primary_key=True)
	formulario= models.OneToOneField(Formulario,on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True, null=True)


	class Meta:
		verbose_name='borrador'
		verbose_name_plural='borradores'

	def __str__(self):
		return str(self.id_borrador)

class ProgramaFirma (models.Model):
	id_programa = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=50)
	created = models.DateTimeField(auto_now_add=True, null=True)

	class Meta:
		verbose_name='programa'
		verbose_name_plural='programas'

	def __str__(self):
		return self.nombre

class ArchivoFirmado (models.Model):
	id_archivo = models.AutoField(primary_key=True)
	borrador= models.OneToOneField(Borrador,on_delete=models.CASCADE)
	programafirma=models.ForeignKey(ProgramaFirma, on_delete=models.CASCADE )
	created = models.DateTimeField(auto_now_add=True, null=True)

	class Meta:
		verbose_name='archivoFirmado'
		
	def __str__(self):
		return str(self.id_archivo)


