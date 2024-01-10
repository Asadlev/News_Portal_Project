from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .models import BaseRegisterForm

from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required


class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'


'''
    Теперь нам нужно добавить ещё одно view для апгрейда аккаунта до Premium. 
    Иными словами, 
    для добавления в группу premium. 
    Для данной задачи не существует дженерика, 
    а писать класс-представление для такой простой задачи кажется избыточным, 
    поэтому напишем функцию-представление.

    В файле sign/views.py добавим её, 
    не забывая импортировать модель групп, 
    и декоратор проверки аутентификации.
'''
@login_required
def upgrade_me(request):
    user = request.user
    author_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        author_group.user_set.add(user)

    return redirect('/')



