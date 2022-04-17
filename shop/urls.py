from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .import views
from .import service


urlpatterns = [
    path('', views.HomePage, name='index'),
    path('shop/', views.ProductViev.as_view(), name='shop'),
    path('filter', views.FilterProductViev.as_view(), name='filter'),
    path('cart/', views.CartView, name='cart'),

    path('shop/<slug:category_slug>', views.CategoryView.as_view(), name='category'),
    path('single/<slug:product_slug>', views.PostDetail.as_view(), name='post_detail'),#конкретный товар
    path('review/<int:pk>/', service.AddReview.as_view(), name='add_rewiew'),

    path('about/', views.About, name='about'),
    path('contact/', views.Contact, name='contact'),

    path('register/', service.register, name='register'),
    path('login/', service.user_login, name='login'),
    path('logout/', service.user_logout, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
