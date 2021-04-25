from django import forms
from apps.produccion.models import Barril   
from django.core.exceptions import ValidationError 

class BarrilForm(forms.ModelForm):

    class Meta:
        model = Barril
        fields = ['capacidad', 'codigo']
        labels = {
        		'capacidad'  :'Capacidad del barril',
        		'codigo':'Codigo del barril',
                
        }

        widgets = {
        		'codigo': forms.TextInput( 
        			attrs=	{
        					'placeholder':'Ingrese el codigo del barril:',
        					'id':'codigo',
                            'class':'form-control',
							'required':'true',
							'type':'number',
                            'autocomplete':'off'
        					}
        			),
        		'capacidad': forms.NumberInput( 
        			attrs=	{
        					'placeholder':'Ingrese la capacidad del del barril',
        					'id':'capacidad',
                            'class':'form-control',
							'min':'0',
							'type':'number',
                            'autocomplete':'off'
        					}
        			)
        }
