from django.shortcuts import render
from .models import *
from catagory.models import *
# Create your views here.
def home(request):
    return render(request,template_name='parent.html',context={})

def productlist(request):
    return render(request, template_name='product/list.html', context={})

def productadd(request):
    context={'catagories':Category.getall()}
    # if(request.method=='POST'):

    return render(request, template_name='product/add.html', context=context)

def productupdate(request,id):
    return render(request, template_name='product/update.html', context={})

def productdel(request,id):
    return render(request, template_name='product/list.html', context={})