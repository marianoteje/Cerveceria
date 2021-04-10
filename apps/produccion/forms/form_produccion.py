from django import forms
from apps.produccion.models import Produccion, Ingrediente_Produccion, Ingrediente

class ProduccionForm(forms.ModelForm):

    class Meta:
        model = Produccion
        fields = ['fecha_produccion', 'cantidad_agua', 'temperatura_maceracion', 'temperatura_coccion', 'tiempo_coccion', 'ingrediente' ]
        labels = {
        		'fecha_produccion'  :'fecha de produccion:',
        		'cantidad_agua':'Cantidad de agua:',
                'temperatura_maceracion'  :'Temperatura de maceracion:',
        		'temperatura_coccion':'Temperatura de coccion:',
                'tiempo_coccion':'Tiempo de coccion:'
                
        }

        widgets = {
        		'fecha_produccion': forms.DateInput( 
        			attrs=	{
        					'placeholder':'Ingrese la fecha de produccion:',
        					'id':'fecha_produccion',
                            'class':'form-control',
        					}
        			),
        		'cantidad_agua': forms.NumberInput( 
        			attrs=	{
        					'placeholder':'Ingrese la cantidad de agua',
        					'id':'cantidad_agua',
                            'class':'form-control'
        					}
        			),
                'temperatura_maceracion': forms.NumberInput( 
        			attrs=	{
        					'placeholder':'Ingrese la temperatura de maceracion:',
        					'id':'temperatura_maceracion',
                            'class':'form-control'
        					}
        			),
        		'tiempo_coccion': forms.TextInput( 
        			attrs=	{
        					'placeholder':'Ingrese el tiempo de coccion',
        					'id':'tiempo_coccion',
                            'class':'form-control'
        					}
        			),
        		'ingrediente': forms.SelectMultiple( 
        			attrs=	{
        					'placeholder':'Ingrese el ingrediente',
        					'id':'ingrediente',
                            'class':'form-control'
        					}
        			)
                
        }
		
