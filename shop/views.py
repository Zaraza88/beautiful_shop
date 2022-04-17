from django.shortcuts import render
from django.views.generic import DetailView
from django.db.models import Q

from .utils import DataMixin
from .models import Category, Product


class ProductViev(DataMixin):
    '''Возвращает список товара на главной странице'''
    
    def get_queryset(self):
        return Product.objects.filter(available=True)


class CategoryView(DataMixin):
    '''Вывод по определенным категориям'''

    def get_queryset(self):
        return Product.objects.filter(
            category__slug=self.kwargs['category_slug']).select_related('category')


class FilterProductViev(DataMixin):
    """Фильтр по 'OperatingSystems', 'Platform', 'Ram'"""

    def get_queryset(self):
        queryset = Product.objects.filter(
            Q(os__in=self.request.GET.getlist('operativ')) | \
            Q(platform__in=self.request.GET.getlist('platform')) | \
            Q(ram__in=self.request.GET.getlist('ram'))
        )
        return queryset


class PostDetail(DetailView):
    '''Вывод конкретного продукта'''

    model = Product
    context_object_name = 'product'
    template_name = 'shop/single.html'
    slug_url_kwarg = 'product_slug'

#-------------------------Скоро это будет все работать-----------------------#
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


def CartView(request):
    return render(request, 'shop/cart.html')