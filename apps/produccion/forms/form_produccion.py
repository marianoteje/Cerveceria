from django import forms
from apps.produccion.models import Produccion


class ProduccionForm(forms.ModelForm):
	class Meta:
		model = Produccion
		fields=(
			'descripcion',
	    	    'fecha_produccion',
				'cantidad_agua',
				'temperatura_maceracion',
				'tiempo_maceracion',
				'temperatura_coccion',
				'tiempo_coccion')

		labels = {
			'descripcion':'Descripcion',
			'fecha_produccion':'Fecha produccion',
			'Cantidad agua':'Litros de agua usados',
			'temperatura_maceracion':'Temperatura macerado',
			'tiempo_maceracion':'Tiempo de macerado',
			'temperatura_coccion':'Temperatura coccion',
			'tiempo_coccion':'Tiempo de coccion'
		}

		widgets ={
			'descripcion': forms.TextInput( 
        			attrs=	{
        					'placeholder':'Ingrese descripcion',
        					'id':'descripcion',
                            'class':'form-control',
							'required':'true'
        					}
        			),
        		'fecha_produccion': forms.TextInput( 
        			attrs=	{
        					'id':'fecha_produccion',
                            'class':'form-control'
        					}
        			),
                'cantidad_agua': forms.NumberInput(
                    attrs= {
                            'placeholder':'Cantida de agua (lts)',
                            'id':'cantidad_agua',
                            'class':'form-control',
							'required':'true'
                    }
                ),
                'temperatura_maceracion': forms.NumberInput(
                    attrs={
                            'placeholder':'Temperatura de macerado',
                            'id':'temperatura_maceracion',
                            'class':'form-control',
							'required':'true'
                            
                    }
                ),
                'tiempo_maceracion': forms.TimeInput(
                    attrs={
                            'placeholder':'Tiempo macerado',
                            'id':'tiempo_maceracion',
                            'class':'form-control',
							'required':'true'
                    }
                ),
                'temperatura_coccion': forms.NumberInput(
                    attrs={
                            'placeholder':'Temperatura de coccion',
                            'id':'temperatura_coccion',
                            'class':'form-control',
							'required':'true'
                    }
                ),
                'tiempo_coccion': forms.TimeInput(
                    attrs={
                            'placeholder':'Tiempo coccion',
                            'id':'tiempo_coccion',
                            'class':'form-control',
							'required':'true'
                    }
                )

		}

	
