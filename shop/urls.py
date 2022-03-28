from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path('', views.HomePage, name='index'),
    path('shop/', views.ProductViev.as_view(), name='shop'),
    path('filter/', views.FilterProductViev.as_view(), name='filter'),
    
    path('shop/<slug:category_slug>', views.CategoryViev.as_view(), name='category'),
    path('single/<slug:product_slug>/', views.PostDetail.as_view(), name='post_detail'),#конкретный товар
    path('review/<int:pk>/', views.AddReview.as_view(), name='add_rewiew'),

    path('about/', views.About, name='about'),
    path('contact/', views.Contact, name='contact'),

    path('register/', views.RegisterUser.as_view(), name='register'),
    path('login/', views.LoginUser.as_view(), name='login'),
    # path('search/', views.Search.as_view(), name='search'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
