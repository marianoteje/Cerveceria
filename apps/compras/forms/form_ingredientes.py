from django import forms
from apps.compras.models import Ingrediente    

class IngredienteForm(forms.ModelForm):

    class Meta:
        model = Ingrediente
        fields = ['nombre', 'stock']
        labels = {
        		'nombre'  :'Nombre del ingrediente',
        		'stock':'Stock',
                
        }

        widgets = {
        		'nombre': forms.TextInput( 
        			attrs=	{
        					'placeholder':'Ingrese el nombre del ingrediente',
        					'id':'nombre',
                            'class':'form-control'
        					}
        			),
        		'stock': forms.TextInput( 
        			attrs=	{
        					'placeholder':'Ingrese el stock',
        					'id':'stock',
                            'class':'form-control'
        					}
        			)
        }
