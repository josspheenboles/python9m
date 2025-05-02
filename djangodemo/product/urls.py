from django.urls import path


from .views import *
urlpatterns=[
    path('',productlist,name='plist'),
    path('Add/',productadd,name='padd'),
    path('Update/<id:int>',productupdate,name='pupdate'),
    path('Delete/<id:int>',productdel,name='pdel'),


]