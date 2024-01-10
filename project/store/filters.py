from django_filters import FilterSet, ModelMultipleChoiceFilter
from .models import Product, Material, ProductMaterial


# Создаем свой набор фильтров для модели Product.
# FilterSet, Который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики
class ProductFilter(FilterSet):
    material = ModelMultipleChoiceFilter(
        field_name='name',
        queryset=Material.objects.all(),
        label='Material',
        conjoined=True,
    )

    class Meta:
        # В Meta классе мы должны указать Django модель,
        # в которой будем фильтровать записи.
        model = Product
        # В fields мы описываем по каким полям модели
        # будет производиться фильтрация.
        fields = {
            # поиск по названию
            'name': ['icontains'],
            # количество товаров должно быть больше или равно
            'quanity': ['gt'],
            'price': [
                'lt',  # цена должна быть меньше или равна указанной
                'gt',  # цена должна быть больше или равна указанной
            ],
        }







