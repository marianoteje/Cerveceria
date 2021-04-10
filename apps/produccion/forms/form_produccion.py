from django import forms
from apps.produccion.models import Produccion, Ingrediente_Produccion, Ingrediente

class ProduccionForm(forms.ModelForm):

    class Meta:
        model = Produccion
        fields = ['descripcion','fecha_produccion', 'cantidad_agua', 'temperatura_maceracion','tiempo_maceracion', 'temperatura_coccion', 'tiempo_coccion', 'ingrediente' ]
        labels = {
				'descripcion'  :'Descripcion:',
        		'fecha_produccion'  :'Fecha de produccion:',
        		'cantidad_agua':'Cantidad de agua:',
                'temperatura_maceracion'  :'Temperatura de maceracion:',
				'tiempo_maceracion'  :'Tiempo de maceracion:',
        		'temperatura_coccion':'Temperatura de coccion:',
                'tiempo_coccion':'Tiempo de coccion:',
				'ingrediente':'Ingrediente:'      
        }

        widgets = {
				'descripcion': forms.TextInput( 
        			attrs=	{
        					'placeholder':'descripcion de la produccion',
        					'id':'descripcion',
                            'class':'form-control',
        					}
        			),
        		'fecha_produccion': forms.DateInput( 
        			attrs=	{
        					'placeholder':'Ingrese la fecha de produccion',
        					'id':'fecha_produccion',
                            'class':'form-control',           
                            'type':'date'
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
				'tiempo_maceracion': forms.NumberInput( 
        			attrs=	{
        					'placeholder':'Tiempo de maceracion:',
        					'id':'tiempo_maceracion',
                            'class':'form-control'
        					}
        			),
				'temperatura_coccion': forms.TextInput( 
        			attrs=	{
        					'placeholder':'Temperatura de la coccion',
        					'id':'temperatura_coccion',
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
		
