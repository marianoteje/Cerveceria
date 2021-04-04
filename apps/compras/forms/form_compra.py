from django import forms
from apps.compras.models import Compra, Proveedor    

class CompraForm(forms.ModelForm):

    
    def __init__(self,*args,**kwargs):
        self.qset = Proveedor.objects.filter(activo=1)
        super(CompraForm,self).__init__(*args,**kwargs)
        self.fields['id_proveedor'].queryset = self.qset
        self.fields['id_proveedor'].empty_label='Elija Proveedor'



    class Meta:
        
        model = Compra

        

        fields = ['id_proveedor','id_ingrediente','costo','fecha_compra','fecha_vencimiento','cantidad','comentario']
        
        labels = {
        		
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

                    }),
        	
        		'id_ingrediente': forms.Select( 
        			attrs=	{

        				    'id':'id_ingrediente',
        					'placeholder':'Ingrese el ingrediente',
        					'class':'form-control'

        					}
        			),
                'costo': forms.NumberInput(
                    attrs= {
                            'placeholder':'Ingrese el costo',
                            'id':'costo',
                            'class':'form-control'
                    }
                ),
                'fecha_compra': forms.DateInput(
                    attrs={
                            'placeholder':'Ingrese la fecha de compra',
                            'class': 'form-control',
                            'id':'fecha_compra',
                            'type':'date'
                    }
                ),
                'fecha_vencimiento': forms.DateInput(
                    attrs={
                            'placeholder':'Ingrese la fecha de vencimiento',
                            'class': 'form-control',
                            'id':'fecha_vencimiento',
                            'type':'date', 
                            'required':'false'
                    }
                ),
                'cantidad': forms.NumberInput(
                    attrs={
                            'placeholder':'Ingrese la cantidad comprada en kilos',
                            'id':'cantidad',
                            'class':'form-control'
                    }
                ),
                'comentario': forms.TextInput(
                    attrs={
                            'placeholder':'Ingrese algun comentario',
                            'id':'comentario',
                            'class':'form-control'
                    }
                )
                
        }

        