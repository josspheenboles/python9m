import sys

from django.shortcuts import render,redirect
from .models import *
from catagory.models import *
from .forms import *
# Create your views here.
def home(request):
    return render(request,template_name='parent.html',context={})

def productlist(request):
    return render(request, template_name='product/list.html', context={'products':Product.getall()})

def productadd(request):
    context={'catagories':Category.getall()}
    if(request.method=='POST'):
        Product.objects.create(
            name=request.POST['name'],
            price=request.POST['price'],
            image=request.FILES['image'],
            isactive=(request.POST['isactive']=='on'),
            catagoryid=Category.getbyid(request.POST['catagoryid']),
        )
        return redirect('plist')
    return render(request, template_name='product/add.html', context=context)

def productupdate(request,id):
    context={'form':ProductForm(instance=Product.getbyid(id))}
    if request.method=='POST':
        form=ProductForm(data=request.POST,instance=Product.getbyid(id))
        if(form.is_bound and form.is_valid()):
            form.save(commit=True)
            return redirect('plist')
        else:
            context['msg']=form.errors
            return render(request, template_name='product/update.html', context=context)
    return render(request, template_name='product/update.html', context=context)

def productdel(request,id):
    prod=Product.getbyid(id)
    if prod:
        Product.objects.filter(pk=id).delete()
    return redirect('plist')
