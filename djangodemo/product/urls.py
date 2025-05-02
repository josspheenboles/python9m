from django.urls import path


from .views import *
urlpatterns=[
    path('',productlist,name='plist'),
    path('Add/',productadd,name='padd'),
    path('Update/<int:id>',productupdate,name='pupdate'),
    path('Delete/<int:id>',productdel,name='pdel'),


]