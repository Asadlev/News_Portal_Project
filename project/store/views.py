# Импортируем класс, который говорит нам о том,
# что в этом представлении мы будем выводить список объектов из БД
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Product, Material, ProductMaterial
from .filters import ProductFilter
from .forms import ProductForm
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.utils.decorators import method_decorator
# from django.shortcuts import render, HttpResponseRedirect


class ProductsList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = Product
    # Поле, которое будет использоваться для сортировки объектов
    ordering = 'name'
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'products.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'products'
    paginate_by = 2  # Вот так мы можем указать(ограничить) кол-во записей на странице

    # Переопределяем функцию получения списка товаров
    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict, который мы рассматривали
        # в этом юните ранее.
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = ProductFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs


    # # Вывод даты и времени
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class ProductDetail(DetailView):
    # Модель та же, но мы хотим получать информацию по отдельности
    model = Product
    # Используем другой шаблон product.html
    template_name = 'product.html'
    # Название обьекта, в которм будет выбранный пользователем продукт
    context_object_name = 'product'


# Добавляем новое представление для создания товаров
class ProductCreate(CreateView):
    # Указываем нашу разработанную форму
    form_class = ProductForm
    # Модель товаров
    model = Product
    # и новый шаблон, в котором используется форма.
    template_name = 'product_edit.html'


# Добавляем представление для изменения товара
class ProductUpdate(UpdateView):
    form_class = ProductForm
    model = Product
    template_name = 'product_edit.html'


# Представление удаляющее товар.
class ProductDelete(DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_list')


# Пример использование метод_декоратор, для предостовление сайта пользователю, при условий аунентификациий
# @method_decorator(login_required, name='dispatch')
# class ProtectedView(TemplateView):
#     template_name = 'prodected_page.html'


# Пример использований миксина LoginRequiredMixin ещё проще.
# Всего лишь необходимо добавить его в списке наследуемых классов при создании представления.
class ProtectedView(LoginRequiredMixin, TemplateView):
    template_name = 'prodected_page.html'










# Создание представления через функций(def, render, HttpsResponseRedirect)
# def create_product(request):
#     form = ProductForm()
#
#     if request.method == 'POST':
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/products')
#
#
#     return render(request, 'product_edit.html', {'form': form})








