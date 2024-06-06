from django.urls import path
from .views import *

urlpatterns = [
    path("", book, name='book'),
    path('info/', book_info, name='book_info'),
    path('add_book/', add_book, name='add_book')
]