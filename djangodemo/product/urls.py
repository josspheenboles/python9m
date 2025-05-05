from django.urls import path
from .api.views import *

from .views import *
urlpatterns=[

    path('',productlist,name='plist'),
    path('Add/',productadd,name='padd'),
    path('Update/<int:id>',productupdate,name='pupdate'),
    path('Delete/<int:id>',productdel,name='pdel'),


    path('API/',GetallProduct),
    path('API/<int:id>',ProductView.as_view()),

]