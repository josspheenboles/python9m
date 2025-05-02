from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,template_name='parent.html',context={})

def productlist(request):
    return render(request, template_name='product/list.html', context={})