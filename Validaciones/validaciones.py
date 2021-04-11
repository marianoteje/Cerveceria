from django.core.exceptions import ValidationError

def validar_numero_negativos(value):
    if value < 0:
        raise ValidationError("El campo no puede recibir valores menores de 0.")
    else:
        return value
