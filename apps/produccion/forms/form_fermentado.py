from django import forms
from apps.produccion.models import Fermentado, Produccion 

class FermentadoForm(forms.ModelForm):

	def __init__(self,*args,**kwargs):
		self.qset = Produccion.objects.filter(activo=True)
		super(FermentadoForm,self).__init__(*args,**kwargs)
		self.fields['produccion'].queryset = self.qset
		self.fields['produccion'].empty_label='Elija una produccion'

	class Meta:
		model = Fermentado
		fields = ['fecha_inicio', 'fecha_fin', 'litros_entrada', 'litros_salida', 'produccion' ]
		labels = {
        		'fecha_inicio'  :'Fecha de inicio',
        		'fecha_fin':'Fecha de fin',
                'litros_entrada'  :'Litros de entrada',
        		'litros_salida':'Litros de salida',
                'produccion':'Produccion',
        }

		widgets = {
        		'fecha_inicio': forms.DateTimeInput( 
        			attrs=	{
        					'placeholder':'Ingrese la fecha de inicio del fermentado:',
        					'id':'datetimepicker1',
                            'class': 'form-control datetimepicker-input',
            				'data-target': '#datetimepicker1',
							'required':'true',
							'type': 'text',
                            'autocomplete':'off'
        					}
        			),
        		'fecha_fin': forms.DateTimeInput( 
        			attrs=	{
        					'placeholder':'Ingrese la fecha de fin del fermentado:',
        					'id':'datetimepicker2',
                            'class': 'form-control datetimepicker-input',
            				'data-target': '#datetimepicker2',
							'required':'true',
							'type': 'text',
                            'autocomplete':'off'
        					}
        			),
                'litros_entrada': forms.NumberInput( 
        			attrs=	{
        					'placeholder':'Ingrese los litros de entrada:',
        					'id':'litros_entrada',
                            'class':'form-control',
							'min':'1',
							'type':'number'
        					}
        			),
        		'litros_salida': forms.NumberInput( 
        			attrs=	{
        					'placeholder':'Ingrese los litros de salida',
        					'id':'litros_salida',
                            'class':'form-control',
							'min':'1',
							'type':'number'
        					}
        			),
                'produccion': forms.Select( 
        			attrs=	{
        					'placeholder':'Produccion',
        					'id':'produccion',
                            'class':'form-control',
							'required':'true'
        					}
        			)
        }
