from django.views.generic import ListView
from django.db.models import Q

from .models import (
    Category, Brand, Product, OperatingSystems, Platform, Ram
)
# from .forms import RatingForm


class DataMixin(ListView):
    """Вывод информации о товаре, фильтрации товара на страницу"""

    model = Product
    context_object_name = 'products'
    template_name = "shop/shop.html"
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['brands'] = Brand.objects.all()
        context['operativ'] = OperatingSystems.objects.all()
        context['platforms'] = Platform.objects.all()
        context['ram'] = Ram.objects.all()
        

        #поиск по названию и бренду
        search_by = self.request.GET.get('query')
        if search_by:
            context['products'] = Product.objects.filter(
                name__icontains=search_by
                )
        return context

