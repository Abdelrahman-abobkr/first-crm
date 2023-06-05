from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from .filters import *
from accounts.decorators import *

# Create your views here.



@login_required(login_url='login')
@admin_only
def index(request):
    customer = Customer.objects.all()
    order = Order.objects.all()
    total_orders = order.count()
    delivered = Order.objects.filter(status='Delivered').count()
    pending = Order.objects.filter(status='Pending').count()
    context = {
        'orders':order,
        'customers':customer,
        'total_orders':total_orders,
        'delivered':delivered,
        'pending':pending,
    }
    return render(request, 'home/index.html', context)



@login_required(login_url='login')
@admin_only
def product(request):
    product = Product.objects.all()
    context = {
        'products':product,
    }
    return render(request, 'home/product.html', context)



@login_required(login_url='login')
@admin_only
def customer(request, slug):
    customer = Customer.objects.get(slug=slug)
    order = customer.order_set.all()
    total_orders = order.count()
    filter = OrderFilter(request.GET, queryset=order)
    order = filter.qs
    context = {
        'customer':customer,
        'orders':order,
        'filter':filter,
        'total_orders':total_orders,
    }
    return render(request, 'home/customer.html', context)



@login_required(login_url='login')
@allowed_users(allowed_rolles=['customer', 'admin'])
def create(request, id):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'))
    customer = Customer.objects.get(id=id)
    form = OrderFormSet(queryset=Order.objects.none(), instance=customer)
    if request.method == 'POST':
        form = OrderFormSet(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'formset':form,
    }
    return render(request, 'home/create.html', context)



@login_required(login_url='login')
@allowed_users(allowed_rolles=['customer', 'admin'])
def update(request, id):
    order = Order.objects.get(id=id)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form':form,
    }
    return render(request, 'home/update.html', context)



@login_required(login_url='login')
@allowed_users(allowed_rolles=['customer', 'admin'])
def delete(request, id):
    order = Order.objects.get(id=id)
    order.delete()
    return redirect('/')