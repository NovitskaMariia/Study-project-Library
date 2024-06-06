from django import forms
from .models import Order

class AddToCartForm(forms.Form):
    book_id = forms.IntegerField(widget=forms.HiddenInput())