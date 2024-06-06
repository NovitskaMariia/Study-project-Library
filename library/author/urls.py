from django.urls import path
from .views import *

urlpatterns = [
    path('', start_author, name='start_author'),
    path('add_author/', add_author, name="add_author"),
    path('remove_author/<int:author_id>/', remove_author, name='remove_author')
]