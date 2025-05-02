from django import forms
from .models import *
class ProductUpdateform(forms.Form):
    name=forms.CharField(max_length=50)
    class Meta:
        fields=['__all__']
        exclude=['name']
        model=Product