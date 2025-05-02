from django.db import models

# Create your models here.
class Product(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50,null=False,unique=False)
    price=models.DecimalField(max_digits=2,decimal_places=1)
    image=models.ImageField(upload_to='product/images/',null=True,blank=True)
    isactive=models.BooleanField(default=True)