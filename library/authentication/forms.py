from django import forms
from .models import CustomUser, ROLE_CHOICES
from django.contrib.auth.hashers import make_password


class CustomUserForm(forms.ModelForm):
    
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'middle_name',
                  'email', 'password', 'secret_key']
        labels = {
            'secret_key': 'Are you a librarian? If so, enter a secret key for librarians'
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Enter your name"}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Enter your last name"}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Enter your middle name"}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder':"Enter email"}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':"Password"}),
            'secret_key': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':"Secret key"}),
        }
        
        def save(self, commit=True):
            user = super(CustomUserForm, self).save(commit=False)
            user.password = make_password(self.cleaned_data['password'])  # Hash the password
            if commit:
                user.save()
            return user
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['secret_key'].required = False
        

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}))
    password = forms.CharField(label='Password', max_length=255, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
   
        
class UpdateUser(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'middle_name', 'role', 'is_active']#
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Enter your name"}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Enter your last name"}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Enter your middle name"}),
            'role':  forms.Select(attrs={'class': 'form-control'}),
            'is-active': forms.Select(attrs={'class': 'form-control'})
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].required = False
        self.fields['last_name'].required = False
        self.fields['middle_name'].required = False
    
