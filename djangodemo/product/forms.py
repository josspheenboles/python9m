from django import forms
from .models import *
class ProductForm(forms.ModelForm):
    # name=forms.CharField(max_length=50)
    class Meta:
        model=Product
        fields='__all__'
        # exclude=['name']
