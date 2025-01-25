from django import template

register = template.Library()

@register.filter
def to_percentage(value):
    try:
        valor = f"{float(value):.2f} %"
        print(valor)
        return valor
    except (ValueError, TypeError):
        return "N/A"  # Manejo de errores si el valor no es un float