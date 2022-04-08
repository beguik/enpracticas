from django import forms 

class InicioForm(forms.Form):
	
	nombre= forms.CharField( max_length = 20,)
	apellido1=forms.CharField(max_length = 20,)
	apellido2 = forms.CharField(max_length = 20,)
	dni=forms.CharField(max_length = 9,)
	formulario = forms.CharField( widget=forms.Textarea)
		