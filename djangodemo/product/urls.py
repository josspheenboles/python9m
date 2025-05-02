from django.urls import path


from .views import *
urlpatterns=[
    path('/',productlist,name='plist'),

]