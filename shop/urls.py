from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .import views
from .import logic


urlpatterns = [
    path('', views.HomePage, name='index'),
    path('shop/', views.ProductViev.as_view(), name='shop'),
    path('filter', views.FilterProductViev.as_view(), name='filter'),
    path('cart/', views.CartView, name='cart'),

    path('shop/<slug:category_slug>', views.CategoryViev.as_view(), name='category'),
    path('single/<slug:product_slug>', views.PostDetail.as_view(), name='post_detail'),#конкретный товар
    path('review/<int:pk>/', logic.AddReview.as_view(), name='add_rewiew'),

    path('about/', views.About, name='about'),
    path('contact/', views.Contact, name='contact'),

    path('register/', logic.register, name='register'),
    path('login/', logic.user_login, name='login'),
    path('logout/', logic.user_logout, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
