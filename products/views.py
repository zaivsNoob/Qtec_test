from django.shortcuts import render,redirect
from django.http import HttpResponse 
from .models import Product
from .filters import ProductFilter

# Create your views here.

def home(request):
    filter = ProductFilter(request.GET, queryset=Product.objects.all())
    products = filter.qs
    
    context={
        'products':products,
        'filter':filter
    }
    return render(request,"products/home.html",context)
