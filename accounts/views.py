from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from home.models import *
from home.forms import *
from .forms import *
from .decorators import *
# Create your views here.



@User_Authenticated
def register(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        email = request.POST['email']
        if User.objects.filter(email=email).exists():
            messages.info(request, 'Email Already Exists Try Another Email')
            return redirect('register')
        else:
            if form.is_valid():
                form.save()
                username = form.cleaned_data['username']
                messages.info(request, f'Account Was Created For {username}')
                new_user = authenticate(username=form.cleaned_data['username'],
                                        password=form.cleaned_data['password1'],)
                login(request, new_user)
                return redirect('/')
    return render(request, 'registration/register.html', {'form':form})



@login_required(login_url='login')
@allowed_users(allowed_rolles=['customer'])
def profile(request):
    order = request.user.customer.order_set.all()
    create = request.user.customer
    context = {
        'orders':order,
        'create':create,
    }
    return render(request, 'accounts/profile.html', context)



@login_required(login_url='login')
@allowed_users(allowed_rolles=['customer'])
def edit_profile(request):
    customer = request.user.customer
    customer_form = CustomerForm(instance=customer)
    user_form = UserInfoForm(instance=request.user)
    if request.method == 'POST':
        user_form = UserInfoForm(request.POST, instance=request.user)
        customer_form = CustomerForm(request.POST, request.FILES, instance=customer)
        if customer_form and user_form.is_valid():
            customer_form.save()
            user_form.save()
            messages.info(request, 'Profile Is Updated')
            return redirect('edit_profile')
    return render(request, 'accounts/edit_profile.html', {'c_form':customer_form, 'u_form': user_form, 'customer':customer})




def view_img(request, slug):
    imagePk = Customer.objects.get(slug=slug)
    imagePkUrl = imagePk.img.url
    return render(request, 'accounts/view_img.html', {'imagePkUrl': imagePkUrl})