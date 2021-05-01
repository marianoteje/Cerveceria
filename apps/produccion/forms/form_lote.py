from django import forms
from apps.produccion.models import Lote, Barril 

class LoteForm(forms.ModelForm):

	class Meta:
		model = Lote
		fields = ['fecha_llenado', 'hora_llenado', 'fecha_carbonatado','hora_carbonatado','barriles','id_produccion']
		labels = {
        		'fecha_llenado'  :'Fecha de llenado de los barriles',
				'hora_llenado'  :'Hora de llenado de los barriles',
				'fecha_carbonatado'  :'Fecha de carbonatado de los barriles',
				'hora_carbonatado'  :'Hora de carbonatado de los barriles',
                'barriles'  :'Barriles del lote',
                'id_produccion'  :'Produccion del lote'
        }

		widgets = {
			
				'fecha_llenado': forms.DateInput( 
        			attrs=	{
        					'placeholder':'Ingrese fecha de llenado de los barriles:',
        					'id':'fecha_llenado',
                            'type':'text', 
                            'class':'form-control',
                            'required':'true',
                            'name':'fecha_llenado',
                            'autocomplete':'off'
						}
        			),
				'hora_llenado': forms.TimeInput( 
        			attrs=	{
        					'placeholder':'Ingrese hora de llenado del lote:',
                            'type':'time', 
                            'class':'form-control',
                            'autocomplete':'off'   
        					}
        			),
        		'fecha_carbonatado': forms.DateInput( 
        			attrs=	{
        					'placeholder':'Ingrese fecha de carbonatado de los barriles:',
        					'id':'fecha_carbonatado',
                            'type':'text',
                            'class':'form-control',
                            'required':'true',
                            'name':'fecha_carbonatado',
                            'autocomplete':'off'   
        					}
        			),
				'hora_carbonatado': forms.TimeInput( 
        			attrs=	{
        					'placeholder':'Ingrese hora de carbonatado del lote:',
                            'type':'time', 
                            'class':'form-control',
                            'autocomplete':'off'   
        					}
        			),
				'barriles': forms.SelectMultiple( 
        			attrs=	{
        					'placeholder':'Ingrese los barriles del lote:', 
                            'class':'form-control',
                            'required':'true',
                            'autocomplete':'off'                            
        					}
        			),
        		'id_produccion': forms.Select( 
        			attrs=	{
        					'placeholder':'Ingrese la produccion del lote:',
                            'class':'form-control',
                            'required':'true',
                            'autocomplete':'off'   
        					}
        			)
        }
