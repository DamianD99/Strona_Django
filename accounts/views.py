from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()

    total_orders = orders.count()
    dostarczone = orders.filter(status='Dostarczone').count()
    pakowane = orders.filter(status='Pakowane').count()

    context = {'orders': orders, 'customers': customers,
               'total_orders': total_orders, 'dostarczone': dostarczone,
               'pakowane': pakowane}

    return render(request, 'accounts/dash.html',context)

def products(request):
    products = Produkty.objects.all()

    return render(request, 'accounts/products.html', {'products': products})


def customer(request):
    return render(request, 'accounts/customer.html')
