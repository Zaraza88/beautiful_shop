from django.db.models import Q

from .models import Category, Brand, Product, OperatingSystems, Platform, Ram

class DataMixin:
    """Миксин для поиска и определения контекста"""

    def get_user_context(self, **kwargs):
        context = kwargs
        context['categories'] = Category.objects.all()
        context['brands'] = Brand.objects.all()
        context['operativ'] = OperatingSystems.objects.all()
        context['platforms'] = Platform.objects.all()
        context['ram'] = Ram.objects.all()

        #поиск по названию и бренду
        search_by = self.request.GET.get('price')
        if search_by:
            context['products'] = Product.objects.filter(name__icontains=search_by)

        return context


# class FilterMixin:
#     """Фильтр"""

#     def get_queryset(self):
#         queryset = Product.objects.filter(
#             Q(manufacturer__in=self.request.GET.getlist('manufacturer')) | \
#             Q(os__in=self.request.GET.getlist('operativ')) | \
#             Q(platform__in=self.request.GET.getlist('platform')) | \
#             Q(ram__in=self.request.GET.getlist('ram'))        
#         )
#         return queryset
