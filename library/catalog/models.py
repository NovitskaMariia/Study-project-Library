from django.db import models
from author.models import Author as OriginalAuthor
from book.models import Book as OriginalBook
from order.models import Order as OriginalOrder
from authentication.models import CustomUser 


class AuthorProxy(OriginalAuthor):
    class Meta:
        proxy = True
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
        

class BookProxy(OriginalBook):
    class Meta:
        proxy = True
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        

class OrderProxy(OriginalOrder):
    class Meta:
        proxy = True
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


class AuthenticationProxy(CustomUser):
    class Meta:
        proxy = True
        verbose_name = 'User'
        verbose_name_plural = 'Users'