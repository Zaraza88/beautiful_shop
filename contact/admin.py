from django.contrib import admin
from .models import ContactModel

# Register your models here.
@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email',]
    list_display_links = ('name',)