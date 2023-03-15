from django.urls import path
from home import views
from shopcart import views as cart_views

urlpatterns = [
    path('', views.index, name='index'),
    path('shop/', views.shop, name='shop'),
    path('shop-detail/<int:id>/', views.shop_detail, name='shop-detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('filter/<str:keyword>/', views.filter_view, name='filter'),
    path('search/', views.search_view, name='search'),
    path('cart/', cart_views.cart_view, name='cart'),

    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),

    path('change-quantity/<int:id>/', cart_views.change_quantity, name='change-quantity'),
    path('remove-cart/<int:id>/', cart_views.remove_cart, name='remove-cart'),
    path('add-cart/<int:id>/', cart_views.add_cart, name='add-cart'),

    path('info/<int:id>/', cart_views.info_view, name='info'),
    path('buy-products/', cart_views.buy_products, name='buy-products'),

    path('to-session/<int:id>/', views.to_session, name='to-session'),
    path('buy-one-product/<int:id>/<int:quantity>/<str:size>/<str:color>/', views.buy_one_product, name='buy-one-product'),
    path('success-page/', cart_views.success_page, name='success-page')
]
