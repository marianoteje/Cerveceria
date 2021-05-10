from django import forms
from apps.ventas.models import Ventas  

class VentaForm(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        super(VentaForm,self).__init__(*args,**kwargs)
        self.fields['forma_de_pago'].empty_label='Selecione la forma de pago'
        self.fields['cliente'].empty_label='Seleccione el cliente'


    class Meta:
        model = Ventas
        fields = ['fecha','descripcion','valor', 'barriles','cliente','forma_de_pago']
        labels = {
        		
        		'fecha':'Fecha de la venta',
                'descripcion':'Descripcion de la venta',
                'valor':'Valor de la venta',
                'barriles':'Barriles',
                'cliente':'Cliente',
                'forma_de_pago':'Forma de pago'
        }

        widgets = {
                'fecha': forms.DateInput(
                    attrs={
                            'placeholder':'Ingrese la fecha de la venta',
                            'id':'fecha_venta',
                            'class':'form-control',
                            'required':'true',
                            'autocomplete':'off',
							'type':'text'
                    }
                ),
        		'descripcion': forms.TextInput( 
        			attrs = {
                            'id':'descripcion',
        					'placeholder':'Ingrese la descripcion de la venta',
        					'class':'form-control',
                            'autocomplete':'off',
        					}
        			),
                'valor': forms.TextInput(
                    attrs={
                            'placeholder':'Ingrese el valor de la venta',
                            'id':'valor',
                            'class':'form-control',
                            'required':'true',
                            'autocomplete':'off',
							'min':'1',
							'type':'number'
                    }
                ),
                'barriles': forms.SelectMultiple(
                    attrs={
                            'placeholder':'Seleccione los barriles',
                            'id':'barriles',
                            'class':'form-control',
                            'required':'true',
                            'autocomplete':'off'
                    }
                ),
                'cliente': forms.Select(
                    attrs={
                            'placeholder':'Elija el cliente de la venta',
                            'id':'cliente',
                            'type':'text', 
                            'class':'form-control',
                            'autocomplete':'off',
                            'required':'true'
                    }
                ),
                'forma_de_pago': forms.Select(
                    attrs={
                            'placeholder':'Elija la forma de pago de la venta',
                            'id':'forma_de_pago',
                            'class':'form-control',
                            'required':'true',
                            'autocomplete':'off'
                            
                    }
                )
                
        }
