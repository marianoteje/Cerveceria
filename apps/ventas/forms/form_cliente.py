from django import forms
from apps.ventas.models import Cliente, Situacion_frente_iva  

class ClientesForm(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        super(ClientesForm,self).__init__(*args,**kwargs)
        self.fields['situacion_frente_iva'].empty_label='Situacion dfrente a IVA'

    class Meta:
        model = Cliente
        fields = ['razon_social','ciudad','telefono', 'email','calle','altura','cuit','situacion_frente_iva', 'comentarios']
        labels = {
        		
        		'razon_social':'Razon social',
                'ciudad':'Ciudad',
                'telefono':'Telefono',
                'email':'Email',
                'calle':'Calle',
                'altura':'Altura',
                'cuit':'CUIT',
                'situacion_frente_iva':'Situacion frente a IVA',
                'comentarios':'Comentarios'    
        }

        widgets = {
                'razon_social': forms.TextInput(
                    attrs={
                            'id':'razon_social',    
                            'placeholder':'Ingrese la razon social del cliente',                       
                            'class':'form-control',
                            'autocomplete':'off',
                            'required':'true'
                    }),
        		'ciudad': forms.TextInput( 
        			attrs={

        				    'id':'ciudad',
        					'placeholder':'Ingrese la ciudad',
        					'class':'form-control',
                            'autocomplete':'off',
                            'required':'true'
        					}
        			),
                'telefono': forms.TextInput(
                    attrs={
                            'placeholder':'Ingrese el costo',
                            'id':'costo',
                            'class':'form-control',
                            'required':'true',
                            'autocomplete':'off',
							'type':'text'
                    }
                ),
                'email': forms.TextInput(
                    attrs={
                            'placeholder':'Ingrese el email del cliente',
                            'id':'costo',
                            'class':'form-control',
                            'required':'true',
                            'autocomplete':'off',
							'type':'email'
                    }
                ),
                'calle': forms.TextInput(
               
                    attrs={
                            'placeholder':'Ingrese la fecha de compra',
                            'id':'datepickerCompra',
                            'type':'text', 
                            'class':'form-control',
                            'autocomplete':'off',
                            'required':'true',
                            'name':'calle',
                    }
                ),
                'altura': forms.TextInput(
                    attrs={
                            'placeholder':'Ingrese la altura de la calle',
                            'id':'altura',
                            'type':'text', 
                            'class':'form-control',
                            'required':'true',
                            'autocomplete':'off',
                            'name':'altura'
                    }
                ),
                'cuit': forms.TextInput(
                    attrs={
                            'placeholder':'Ingrese el CUIT del cliente',
                            'id':'cuit',
                            'class':'form-control',
                            'required':'true',
                            'autocomplete':'off'
                    }
                ),
                'comentarios': forms.TextInput(
                    attrs={
                            'placeholder':'Ingrese algun comentario',
                            'id':'comentario',
                            'class':'form-control',
                            'autocomplete':'off'
                    }
                ),
                'situacion_frente_iva': forms.Select(
                    attrs={
                            'placeholder':'Ingrese la situacion frente a IVA',
                            'id':'situacion_frente_iva',
                            'class':'form-control',
                            'autocomplete':'off'
                    }
                )
                
        }

        