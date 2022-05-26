from django.db import models

# Create your models here.
from users.models import CustomUser


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()

class Order(models.Model):
    haridor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE)
