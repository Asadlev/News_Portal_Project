from django import forms
from .models import Product
from django.core.exceptions import ValidationError




class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        # fields = '__all__'
        # В место <__all__> мы могли бы перечислить все поля:

        fields = [
           'name',
           'discription',
           'quanity',
           'category',
           'price',
       ]



        # Но мы не стали так делать,
        # потому что метод __all__ Перебирает все поля модели

        '''
        Совет от автора
        
        Для рабочих проектов советуем всё-таки потратить время и перечислить поля, 
        чтобы не было ситуации, 
        что вы добавили новое поле в модель, 
        которое нельзя редактировать пользователям, 
        а из-за fields = ‘__all__’ это поле стало автоматически доступным для редактирования через форму. Примером такого поля может быть время создания товара. Странно, если пользователь будет иметь возможность его редактировать.
        В зависимости от того, 
        как мы расположим поля в списке, 
        в таком порядке они и будут выведены на странице. 
        Это значит, мы сможем удобнее и логичнее вывести данные для заполнения.
        '''
    # def clean(self):
    #     cleaned_data = super().clean()
    #     discription = cleaned_data.get('discription')
    #     if discription is not None and len(discription) < 20:
    #         raise ValidationError({
    #             'discription': 'Описание не может быть менее 20 символов.'
    #         })
    #
    #     name = cleaned_data.get("name")
    #     if name == discription:
    #         raise ValidationError(
    #             "Описание не должно быть идентичным названию."
    #         )
    #
    #     return cleaned_data

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        discription = cleaned_data.get("discription")

        if name == discription:
            raise ValidationError(
                "Описание не должно быть идентичным названию."
            )

        return cleaned_data

    ''' вот так мы можем проверить, написано ли название товара с заглавной буквы: '''
    def clean_name(self):
        name = self.cleaned_data['name']
        if name[0].islower():
            raise ValidationError(
                'Название должно начинаться с заглавной буквы.'
            )

        return name





