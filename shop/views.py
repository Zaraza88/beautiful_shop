from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from django.db.models import Q
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, logout


from .utils import DataMixin
from .forms import ReviewForm, LoginForm, RegisterForm
from .models import Category, Product


class ProductViev(DataMixin, ListView):
    '''Возвращает список товара на главной странице'''

    model = Product
    context_object_name = 'products'
    template_name = "shop/shop.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        get_category = self.get_user_context()
        return dict(list(context.items()) + list(get_category.items()))

    def get_queryset(self):
        return Product.objects.filter(available=True)


class FilterProductViev(ProductViev):
    """Фильтр"""

    def get_queryset(self):
        queryset = Product.objects.filter(
            Q(manufacturer__in=self.request.GET.getlist('manufacturer')) | \
            Q(os__in=self.request.GET.getlist('operativ')) | \
            Q(platform__in=self.request.GET.getlist('platform')) | \
            Q(ram__in=self.request.GET.getlist('ram'))        
        )
        return queryset
# class Search(ProductViev):
#     '''Поиск по названию и бренду товара'''

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         get_category = self.get_user_context()

#         search_by = self.request.GET.get('query')
#         if search_by:
#             search = Product.objects.filter(
#                 Q(name__icontains=search_by) | Q(manufacturer__icontains=search_by)
#             )
#             context['products'] = search
#         return dict(list(context.items()) + list(get_category.items()))


class CategoryViev(DataMixin, ListView):
    '''Вывод по определенным категориям'''

    model = Product
    context_object_name = 'products'
    template_name = "shop/shop.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        get_category = self.get_user_context()
        return dict(list(get_category.items()) + list(context.items()))

    #выводит продукт категории по клику на категори
    def get_queryset(self):
        return Product.objects.filter(
            category__slug=self.kwargs['category_slug']).select_related('category')


class PostDetail(DetailView):
    '''Вывод конкретного продукта'''

    model = Product
    context_object_name = 'product'
    template_name = 'shop/single.html'
    slug_url_kwarg = 'product_slug'


class AddReview(View):
    """Отзывы"""

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        product = Product.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.product = product
            form.save()
        return redirect(product.get_absolute_url())


def About(request):
    return render(request, 'shop/about.html')

def Contact(request):
    return render(request, 'shop/contact.html')

def HomePage(request):
    products = Product.objects.all()[:3]
    categories = Category.objects.all()[:3]

    return render(request, 'shop/index.html', {'products': products, 'categories': categories})





def test(request):
    return render(request, 'shop/test.html')


class RegisterUser(CreateView):
    """Регистрация пользователя"""
    form_class = RegisterForm
    template_name = 'shop/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    """Авторизация пользователя"""

    form_class = LoginForm
    template_name = 'shop/login.html'

    def get_success_url(self) -> str:
        return reverse_lazy('home')


def user_logout(request):
    logout(request)
    return redirect('login')