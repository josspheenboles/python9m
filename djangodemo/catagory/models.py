from django.db import models
import uuid
# Create your models here.
class Category(models.Model):
    """Hierarchical category system with advanced features"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=150)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='categories/images/', null=True, blank=True)