from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

def home(request):
    return render(request, 'accounts/home.html')


def products(request):
    return render(request, 'accounts/products.html')


def customer(request):
    return render(request, 'accounts/customer.html')
