from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser
from django.contrib import messages
from .forms import CustomUserForm, LoginForm, UpdateUser


def user_login(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']

        try:
            user = CustomUser.objects.get(email=email)
            if user.password == password:
                login(request, user)
                return redirect('login_succssed', user_id=user.id)
            else:
                raise CustomUser.DoesNotExist
        except CustomUser.DoesNotExist:
            messages.error(request, 'Invalid email or password.')

    return render(request, 'authentication/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            new_user = CustomUser.create(**form.cleaned_data)
            login(request, new_user)
            return redirect('success', user_id=new_user.id)
        else:
            form = CustomUserForm()
            return render(request, 'authentication/register.html', {'error': 'Your secret key incorrect'}, {'form':form})
    
    else:
        form = CustomUserForm()
        return render(request, 'authentication/register.html', {'form':form})


def success(request, user_id):
    user = CustomUser.objects.get(pk=user_id)
    return render(request, 'authentication/success.html', {'user': user})


def login_succssed(request, user_id):
    user = CustomUser.objects.get(pk=user_id)
    context = {'user': user, 'role': user.role}
    return render(request, 'authentication/login_succssed.html', context)


def user_logout(request):
    logout(request)
    return redirect('login')


def all_users(request):
    users = CustomUser.get_all().order_by('id')
    return render(request, 'authentication/all_users.html', {'users': users})


def user_info(request):
    user_id = request.GET.get('id')
    user = get_object_or_404(CustomUser, id=user_id)
    
    if request.method == 'POST':
        form = UpdateUser(request.POST, instance=user)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            
            first_name = cleaned_data.get('first_name')
            last_name = cleaned_data.get('last_name')
            middle_name = cleaned_data.get('middle_name')
            role = cleaned_data.get('role')
            is_active = cleaned_data.get('is_active')

            
            user.update(
                first_name=first_name if first_name else None,
                last_name=last_name if last_name else None,
                middle_name=middle_name if middle_name else None,
                role=role,
                is_active=is_active
            )
            user_id = request.GET.get('id')
            user = get_object_or_404(CustomUser, id=user_id)
            return render(request, 'authentication/user_info.html', {'user_upd': user, 'form':form})
        else:
            messages.error(request, 'Invalid email or password.')
    else:
        form = UpdateUser()
    return render(request, 'authentication/user_info.html', {'user_upd': user , 'form':form})
