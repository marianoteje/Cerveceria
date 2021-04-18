from django import forms
from apps.compras.models import Ingrediente    

class IngredienteForm(forms.ModelForm):

    class Meta:
        model = Ingrediente
        fields = ['nombre']
        labels = {
        		'nombre'  :'Nombre del ingrediente'
        	
                
        }

        widgets = {
        		'nombre': forms.TextInput( 
        			attrs=	{
        					'placeholder':'Ingrese el nombre del ingrediente',
        					'id':'nombre',
                            'class':'form-control',
							'required':'true'
        					}
        			)
        }
