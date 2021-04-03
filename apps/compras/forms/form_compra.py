from django import forms
from apps.compras.models import Compra, Proveedor    

class CompraForm(forms.ModelForm):


    class Meta:
        
        model = Compra
        fields = ['id_proveedor', 'id_ingrediente','costo','fecha_compra','fecha_vencimiento','cantidad','comentario']
        labels = {
        		'id_proveedor'  :'Proveedor',
        		'id_ingrediente':'Ingrediente',
                'costo':'Costo',
                'fecha_compra':'Fecha de compra',
                'fecha_vencimiento':'Fecha de vencimiento',
                'cantidad':'Cantidad',
                'comentario':'Comentarios'    
        }

        widgets = {
        		'id_proveedor': forms.Select( 
        			attrs=	{
        					'id':'id_proveedor',
                            
        					}
        			),
        		'id_ingrediente': forms.Select( 
        			attrs=	{
        				    'id':'id_ingrediente'
        					}
        			),
                'costo': forms.NumberInput(
                    attrs= {
                            'placeholder':'Ingrese el costo',
                            'id':'costo'
                    }
                ),
                'fecha_compra': forms.DateInput(
                    attrs={
                            'placeholder':'Ingrese la fecha de compra',
                            'id':'fecha_compra'
                    }
                ),
                'fecha_vencimiento': forms.DateInput(
                    attrs={
                            'placeholder':'Ingrese la fecha de vencimiento',
                            'id':'fecha_vencimiento'
                    }
                ),
                'cantidad': forms.NumberInput(
                    attrs={
                            'placeholder':'Ingrese la cantidad comprada',
                            'id':'cantidad'
                    }
                ),
                'comentario': forms.TextInput(
                    attrs={
                            'placeholder':'Ingrese algun comentario',
                            'id':'comentario'
                    }
                )
                
        }

        