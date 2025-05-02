from django.db import models
from catagory.models import Category
# Create your models here.
class Product(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50,null=False,unique=False)
    # price=models.DecimalField(max_digits=2,decimal_places=1)
    image=models.ImageField(upload_to='product/images/',null=True,blank=True)
    isactive=models.BooleanField(default=True)
    catagoryid=models.ForeignKey(Category,on_delete=models.CASCADE)
    @classmethod
    def getall(cls):
        return cls.objects.all()
    @classmethod
    def getbyid(cls,id):
        return cls.objects.get(pk=id)

    def __str__(self):
        return self.name