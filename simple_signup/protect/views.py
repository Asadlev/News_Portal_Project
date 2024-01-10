from django.shortcuts import render
from django.views.generic import TemplateView, View, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'protect/index.html'

    # Добавляем функцию, которая отображает кнопку(хочу в группу premium, если я не там!)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_premium'] = not self.request.user.groups.filter(name='premium').exists()
        return context


'''
    Ограничение прав доступа
    На самом деле, в этом ничего сложного нет.
    Мы уже знакомились с миксином LoginRequiredMixin. 
    Так вот предоставление прав не отличается практически ничем.
    
    В классе-представлении мы должны добавить миксин PermissionRequiredMixin:
'''
class MyView(PermissionRequiredMixin, View):
    permission_required = ('<app>.<action>_<model>',
                           '<app>.<action>_<model>',)


class AddProduct(PermissionRequiredMixin, CreateView):
    permission_required = ('shop.add_product', )
    # а дальше пишите код вашего представления




