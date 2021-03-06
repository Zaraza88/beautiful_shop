from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import(
    Product,
    Category, 
    Reviews, 
    Rating, 
    RatingStar, 
    ProductShots, 
    Brand, 
    OperatingSystems, 
    Platform, 
    Ram
    )


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'image']


@admin.register(ProductShots)
class ProductShotsAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'product', 'get_image']
    readonly_fields = ['get_image']


    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} wigth="50" height="60"')



@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ['email', 'name', 'date', 'product']
    ordering = ['-date']
    list_per_page = 10

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ('manufacturer', 'name')
    list_display = [
        'name', 
        'manufacturer', 
        'model', 
        'price', 
        'stock', 
        'available', 
        'get_image',
        'created', 
        'updated', 
        'reting_status'
    ]
    list_filter = ['available', 'created', 'updated', 'manufacturer']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 10
    readonly_fields = ['get_image']

    @admin.display(ordering='price', description='Статус')
    def reting_status(self, product: Product):
        if product.price < 500:
            return 'До 500р.'
        elif 500 >= product.price < 1000:
            return 'От 500р. до 1000р.'
        elif 1000 >= product.price < 2000:
            return 'От 1000р до 2000р.'
        elif 2000 >= product.price < 5000:
            return 'От 2000р. до 5000р.'            
        return 'Свыше 5000р.'

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} wigth="50" height="60"')

    get_image.short_description = 'Дополнительное фото'


admin.site.register(RatingStar)
admin.site.register(OperatingSystems)
admin.site.register(Ram)
admin.site.register(Platform)
admin.site.register(Rating)

admin.site.site_title = 'Django Магазин'
admin.site.site_header = 'Django Магазин'




