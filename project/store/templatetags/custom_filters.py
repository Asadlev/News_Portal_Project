from django import template


register = template.Library()


VALUTE_NAME = {
    'rub': 'P',
    'usd': '$',
}

# Регистрируем наш фильтр под именем currency, чтоб Django понимал,
# что это именно фильтр для шаблонов, а не простая функция.
@register.filter()
def currency(value, code='rub'):
    """
    value: Значение, к которому нужно применить фильтр
    """
    valute = VALUTE_NAME[code]

    return f'{value} {valute}'


@register.filter()
def my_filter(value):

    return f'{value} Штук.'



