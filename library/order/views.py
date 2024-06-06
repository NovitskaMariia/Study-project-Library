from django.shortcuts import render, redirect, get_object_or_404
from .models import Order
from book.models import Book
from authentication.models import CustomUser
from datetime import datetime, timedelta
from .forms import AddToCartForm


def my_cart(request):
    user = request.user  # Отримати поточного користувача

    user_orders = Order.objects.filter(user=user)  # Отримати всі замовлення користувача
    return render(request, 'order/my_cart.html', {'user_orders': user_orders})


def add_to_cart(request, book_id):
    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            user = request.user
            if user.is_authenticated and user.role == 0:
                book_id = form.cleaned_data['book_id']
                book = Book.objects.get(id=book_id)
                current_datetime = datetime.now()
                plated_end_at = current_datetime + timedelta(days=14)

                # Викликайте ваш метод create для створення замовлення
                Order.create(user=user, book=book, plated_end_at=plated_end_at)

    # Перенаправлення на поточну сторінку або іншу сторінку
    return redirect(request.META.get('HTTP_REFERER', 'book'))


def remove_from_order(request, book_id):
    if request.method == 'POST':
        # Отримати об'єкт Order за book_id
        order = Order.objects.filter(book__id=book_id, user=request.user, end_at=None).first()

        # Перевірка, чи існує такий об'єкт
        if order:
            # Видалити об'єкт Order
            order.delete()

    # Перенаправлення на поточну сторінку або іншу сторінку
    return redirect(request.META.get('HTTP_REFERER', 'my_cart'))


def all_orders(request):
    us1 = request.user.role
    all_orders1 = Order.get_all()
    context = {'all_orders': all_orders1, 'role': us1, 'active_page': 'orders'}
    return render(request, 'order/all_orders.html', context)


def all_user_orders(request):
    us1 = request.user.role
    if us1 == 0:
        all_orders2 = Order.objects.filter(user=request.user)
        context = {'all_user_orders': all_orders2, 'role': us1, 'active_page': 'orders'}
        return render(request, 'all_user_orders/all_user_orders.html', context)
    else:
        return redirect('/book')


def delete_order(request, order_id):
    Order.delete_by_id(order_id)
    return redirect('/orders')