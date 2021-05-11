from django import forms
from apps.compras.models import Compra, Proveedor    

class CompraForm(forms.ModelForm):
    class Meta:
        
        model = Compra

        fields = ['id_proveedor','id_ingrediente','costo','fecha_compra','fecha_vencimiento','cantidad','comentario']
        
        labels = {
        		'id_proveedor':'Proveedor',
        		'id_ingrediente':'Ingrediente',
                'costo':'Costo',
                'fecha_compra':'Fecha de compra',
                'fecha_vencimiento':'Fecha de vencimiento',
                'cantidad':'Cantidad',
                'comentario':'Comentarios'    
        }

        widgets = {

                'id_proveedor': forms.Select(
                    attrs={
                            'id':'id_proveedor',                           
                            'class':'form-control',
                            'autocomplete':'off'

                    }),
        	
        		'id_ingrediente': forms.Select( 
        			attrs=	{

        				    'id':'id_ingrediente',
        					'placeholder':'Ingrese el ingrediente',
        					'class':'form-control',
                            'autocomplete':'off'

        					}
        			),
                'costo': forms.NumberInput(
                    attrs= {
                            'placeholder':'Ingrese el costo de la compra',
                            'id':'costo',
                            'class':'form-control',
							'min':'1',
							'type':'number'
                    }
                ),
                'fecha_compra': forms.DateInput(
               
                    attrs={
                            'placeholder':'Ingrese la fecha de compra',
                            'id':'datepickerCompra',
                            'type':'text', 
                            'class':'form-control',
                            'required':'true',
                            'name':'fecha_compra',
                            'autocomplete':'off'
                    }
                ),
                'fecha_vencimiento': forms.DateInput(
                    attrs={
                            'placeholder':'Ingrese la fecha de vencimiento',
                            'id':'datepickerVencimiento',
                            'type':'text', 
                            'class':'form-control',
                            'required':'false',
                            'name':'fecha_vencimiento',
                            'autocomplete':'off'
                    }
                ),
                'cantidad': forms.NumberInput(
                    attrs={
                            'placeholder':'Ingrese la cantidad comprada en kilos',
                            'id':'cantidad',
                            'class':'form-control',
							'min':'1',
                            'autocomplete':'off'
                    }
                ),
                'comentario': forms.TextInput(
                    attrs={
                            'placeholder':'Ingrese algun comentario de la compra',
                            'id':'comentario',
                            'class':'form-control',
                            'autocomplete':'off'
                    }
                )
                
        }

        