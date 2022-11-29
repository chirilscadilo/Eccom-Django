from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('create-card/', views.create_card, name='create-card'),
    path('update-card/<str:pk>', views.update_card, name='update-card'),
    path('delete-card/<str:pk>', views.delete_card, name='delete-card'),
    path('product-card/<str:pk>', views.product_card, name='product-card'),
    
    path('order/', views.order, name='order'),
    path('add-orderItem/<str:pk>', views.add_orderItem, name='add-orderItem'),
    path('update-orderItem/<str:pk>', views.update_orderItem, name='update-orderItem'),
    path('delete-orderItem/<str:pk>', views.delete_orderItem, name='delete-orderItem'),
    path('checkout/', views.chekout, name='checkout'),
]