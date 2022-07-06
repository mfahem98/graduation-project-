from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
    path('', views.index),
    path('add', views.add_new_movie),
    path('good', views.good),
    path('fibuy/<int:id>', views.order_ticket),
    path('customerlogin', LoginView.as_view(template_name='customerlogin.html'),name='customerlogin'),
    path('fibuy', views.final),
    path('logout', LogoutView.as_view(template_name='logout.html'),name='logout'),
    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),
    path('view-customer', views.view_customer_view,name='view-customer'),
    path('delete-customer/<int:pk>', views.delete_customer_view,name='delete-customer'),
    path('update-customer/<int:pk>', views.update_customer_view,name='update-customer'),
    path('admin-products', views.admin_movies_view,name='admin-products'),
    path('admin-add-product', views.add_new_movie,name='admin-add-product'),
    path('delete-product/<int:pk>', views.delete_product_view,name='delete-product'),
    path('update-product/<int:pk>', views.update_product_view,name='update-product'),
    path('admin-view-booking', views.admin_view_order_view,name='admin-view-booking'),
    path('delete-order/<int:pk>', views.delete_order_view,name='delete-order'),
    path('customersignup', views.user_register),

]
