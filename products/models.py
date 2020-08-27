from django.db import models
from django.contrib.auth.models import User
import uuid






# Create your models here.

class Product(models.Model):
    code = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=50, unique=True, default="defaultName")
    model = models.CharField(max_length=50, default="product")
    cost = models.IntegerField()
    selling_price = models.IntegerField()
    size = models.CharField(max_length=10)
    img = models.ImageField(upload_to="product_img/", default="product_img/default.png")
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=50, unique=True)
    telephone_number = models.IntegerField()

    def __str__(self):
        return self.name



class AddTransaction(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    product_code = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_code", to_field="code", db_column="code", default="code")
    quantity = models.IntegerField()
    
    def __str__(self):
        return self.product_code.name
