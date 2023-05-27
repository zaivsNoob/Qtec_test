from django.db import models
from .utility import warranty_choices,category_choices
# Create your models here.


class Product(models.Model):
    name=models.CharField(max_length=200,null='true',blank='true')
    price=models.FloatField(null='true')
    category=models.CharField(max_length=20,choices=category_choices,blank='true')
    warranty=models.IntegerField(choices=warranty_choices)
    
    def __str__(self):
        return self.name