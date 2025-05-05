from django.urls import path
from .api.views import *
from rest_framework.routers import DefaultRouter
from .views import *

router=DefaultRouter()
router.register(r'Prod/',ProductViewSet)



urlpatterns=[

    path('',productlist,name='plist'),
    path('Add/',productadd,name='padd'),
    path('Update/<int:id>',productupdate,name='pupdate'),
    path('Delete/<int:id>',productdel,name='pdel'),


    path('API/',GetallProduct),
    # path('API/<int:id>',ProductView.as_view()),
    path('API/<int:pk>',ProductRetrieveUpdateAPIView.as_view()),

]+router.urls