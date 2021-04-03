from django import forms
from apps.compras.models import Proveedor    

class ProveedorForm(forms.ModelForm):

    class Meta:
        model = Proveedor
        fields = ['nombre', 'descripcion','telefono','email','direccion']
        labels = {
        		'nombre'  :'Nombre del proveedor',
        		'descripcion':'Descripcion',
                'telefono':'Telefono',
                'email':'Email',
                'direccion':'Direccion'
        }

        widgets = {
        		'nombre': forms.TextInput( 
        			attrs=	{
        					'placeholder':'Ingrese el nombre del proveedor',
        					'id':'nombre',
                            
        					}
        			),
        		'descripcion': forms.TextInput( 
        			attrs=	{
        					'placeholder':'Ingrese descripcion',
        					'id':'descripcion'
        					}
        			),
                'telefono': forms.TextInput(
                    attrs= {
                            'placeholder':'Ingrese telefono',
                            'id':'telefono'
                    }
                ),
                'email': forms.EmailInput(
                    attrs={
                            'placeholder':'Ingrese email',
                            'id':'email'
                    }
                ),
                'direccion': forms.TextInput(
                    attrs={
                            'placeholder':'Ingrese direccion',
                            'id':'Ingrese direccion'
                    }
                )
        }
