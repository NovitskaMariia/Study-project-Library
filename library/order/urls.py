from django.urls import path, include
from .views import *

urlpatterns = [
    path('', all_orders, name='all_orders'),
    path('my_cart', my_cart, name='my_cart'),#my
    path('add_to_cart/<int:book_id>/', add_to_cart, name='add_to_cart'), #my
    path('remove_from_order/<int:book_id>/', remove_from_order, name='remove_from_order'), #my
    path('delete_order/<int:order_id>/', delete_order, name='delete_order')
]