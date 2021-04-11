from django import forms
from apps.produccion.models import Produccion, Ingrediente_Produccion, Ingrediente

class ProduccionForm(forms.Form):
	descripcion = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	
	fecha_produccion = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class':'form-control'}))
	
	cant_agua = forms.DecimalField(max_digits=11, decimal_places=2,label='Cantidad agua',
	    widget=forms.NumberInput(attrs={'class':'form-control'}))
	
	temp_maceracion = forms.DecimalField(max_digits=5,decimal_places=2,label='Temperatura de macerado',
	    widget=forms.NumberInput(attrs={'class':'form-control'}))
	
	tiempo_maceracion = forms.DurationField(label='Tiempo de macerado',widget=forms.TextInput(attrs={'class':'form-control'}))
	
	temp_coccion = forms.DecimalField(max_digits=5,decimal_places=2,label='Temperatura de cocción',
	    widget=forms.NumberInput(attrs={'class':'form-control'}))
	
	tiempo_coccion = forms.DurationField(label='Tiempo de cocción',
	    widget=forms.NumberInput(attrs={'class':'form-control'}))

	ingrediente = forms.ModelChoiceField(label='Elija ingrediente',queryset=Ingrediente.objects.filter(activo=1),
	   empty_label='(Elija ingrediente)',widget=forms.Select(attrs={'class':''}))	
	   
	cantidad = forms.DecimalField(max_digits=7,decimal_places=2,min_value=0,widget=forms.NumberInput(attrs={'class':''}))

