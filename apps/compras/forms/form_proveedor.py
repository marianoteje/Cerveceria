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
                            'class':'form-control'
        					}
        			),
        		'descripcion': forms.TextInput( 
        			attrs=	{
        					'placeholder':'Ingrese descripcion',
        					'id':'descripcion',
                            'class':'form-control'
        					}
        			),
                'telefono': forms.TextInput(
                    attrs= {
                            'placeholder':'Ingrese telefono',
                            'id':'telefono',
                            'class':'form-control'
                    }
                ),
                'email': forms.EmailInput(
                    attrs={
                            'placeholder':'Ingrese email',
                            'id':'email',
                            'type': 'email',
                            'class':'form-control'
                    }
                ),
                'direccion': forms.TextInput(
                    attrs={
                            'placeholder':'Ingrese direccion',
                            'id':'Ingrese direccion',
                            'class':'form-control'
                    }
                )
        }
