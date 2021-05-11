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
		fields = ['fecha_inicio', 'fecha_fin','hora_inicio', 'hora_fin', 'litros_entrada', 'litros_salida', 'produccion' ]
		labels = {
        		'fecha_inicio'  :'Fecha de inicio',
				'hora_inicio'  :'Hora de inicio',
                'fecha_fin'  :'Fecha de fin',
                'hora_fin'  :'Hora de fin',
				'litros_entrada'  :'Litros de entrada',
        		'litros_salida':'Litros de salida',
                'produccion':'Produccion'

        }

		widgets = {
				'fecha_inicio': forms.DateInput( 
        			attrs=	{
        					'placeholder':'Ingrese fecha de inicio del fermentado:',
        					'id':'datepickerFechaInicio',
                            'type':'text', 
                            'class':'form-control',
                            'required':'true',
                            'name':'fecha_compra',
                            'autocomplete':'off'
						}
        			),
        		'fecha_fin': forms.DateInput( 
        			attrs=	{
        					'placeholder':'Ingrese fecha de fin del fermentado:',
        					'id':'datepickerFechaFin',
                            'type':'text',
                            'class':'form-control',
                            'required':'true',
                            'name':'meeting-time',
                            'autocomplete':'off'   
        					}
        			),
				'hora_inicio': forms.TimeInput( 
        			attrs=	{
        					'placeholder':'Ingrese hora de inicio del fermentado:',
                            'type':'time', 
                            'class':'form-control',
                            'required':'true',
                            'autocomplete':'off'                            
        					}
        			),
        		'hora_fin': forms.TimeInput( 
        			attrs=	{
        					'placeholder':'Ingrese hora de fin del fermentado:',
                            'type':'time', 
                            'class':'form-control',
                            'required':'true',
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
