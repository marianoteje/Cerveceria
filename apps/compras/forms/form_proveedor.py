from django import forms
from apps.compras.models import Proveedor    

class ProveedorForm(forms.ModelForm):

    class Meta:
        model = Proveedor
        fields = ['nombre', 'descripcion', 'ciudad','telefono','email','direccion']
        labels = {
        		'nombre'  :'Nombre del proveedor',
        		'descripcion':'Descripcion',
                'ciudad':'Ciudad',
                'telefono':'Telefono',
                'email':'Email',
                'direccion':'Direccion'
        }

        widgets = {
        		'nombre': forms.TextInput( 
        			attrs=	{
        					'placeholder':'Ingrese el nombre del proveedor',
        					'id':'nombre',
                            'class':'form-control',
							'required':'true',
                            'autocomplete':'off'
        					}
        			),
        		'descripcion': forms.TextInput( 
        			attrs=	{
        					'placeholder':'Ingrese descripcion del proveedor',
        					'id':'descripcion',
                            'class':'form-control',
                            'autocomplete':'off'
        					}
        			),
                'ciudad': forms.TextInput( 
        			attrs={

        				    'id':'ciudad',
        					'placeholder':'Ingrese la ciudad del proveedor',
        					'class':'form-control',
                            'autocomplete':'off',
        					}
        			),
                'telefono': forms.TextInput(
                    attrs= {
                            'placeholder':'Ingrese telefono del proveedor',
                            'id':'telefono',
                            'class':'form-control',
							'required':'true',
                            'autocomplete':'off'
                    }
                ),
                'email': forms.EmailInput(
                    attrs={
                            'placeholder':'Ingrese email del proveedor',
                            'id':'email',
                            'type': 'email',
                            'class':'form-control',
							'required':'true',
                            'type':'email',
                            'autocomplete':'off'
                    }
                ),
                'direccion': forms.TextInput(
                    attrs={
                            'placeholder':'Ingrese direccion del proveedor',
                            'id':'Ingrese direccion',
                            'class':'form-control',
							'required':'true',
                            'autocomplete':'off'
                    }
                )
        }
