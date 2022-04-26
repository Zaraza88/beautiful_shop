from django.urls import path

from . import views
#не забыть сделать кэш

urlpatterns = [
    path('feedback/', views.CreateContact.as_view(), name='feedback'),
]