from django import forms
from apps.produccion.models import Fermentado, Produccion 

class FermentadoForm(forms.ModelForm):

    class Meta:
        model = Fermentado
        fields = ['fecha_inicio', 'fecha_fin', 'litros_entrada', 'litros_salida', 'produccion' ]
        labels = {
        		'fecha_inicio'  :'Fecha de inicio',
        		'fecha_fin':'Fecha de fin',
                'litros_entrada'  :'Litros de entrada',
        		'litros_salida':'Litros de salida',
                'produccion':'produccion',
        }

        widgets = {
        		'fecha_inicio': forms.DateInput( 
        			attrs=	{
        					'placeholder':'Ingrese la fecha de inicio del fermentado:',
        					'id':'fecha_inicio',
                            'class':'form-control',           
                            'type':'date'
        					}
        			),
        		'fecha_fin': forms.DateInput( 
        			attrs=	{
        					'placeholder':'Ingrese la fecha de fin del fermentado',
        					'id':'fecha_fin',
                            'class':'form-control',           
                            'type':'date'
        					}
        			),
                'litros_entrada': forms.NumberInput( 
        			attrs=	{
        					'placeholder':'Ingrese los litros de entrada:',
        					'id':'litros_entrada',
                            'class':'form-control'
        					}
        			),
        		'litros_salida': forms.NumberInput( 
        			attrs=	{
        					'placeholder':'Ingrese los litros de salida',
        					'id':'litros_salida',
                            'class':'form-control'
        					}
        			),
                'produccion': forms.Select( 
        			attrs=	{
        					'placeholder':'produccion',
        					'id':'produccion',
                            'class':'form-control'
        					}
        			)
        }
