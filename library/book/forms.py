from django import forms
from .models import Book

class BookForm(forms.ModelForm):
     class Meta:
        model = Book
        fields = ['name', 'description', 'count', 'year_of_publish']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Enter book name"}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Enter book description"}),
            'count': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':"Enter books quantity"}),
            'year_of_publish': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':"Enter year"})
        }
        
        
