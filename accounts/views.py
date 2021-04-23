from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

def home(response):
    return render(response, 'accounts/home.html')


def products(response):
    return render(response, 'accounts/products.html')


def customer(response):
    return render(response, 'accounts/customer.html')
