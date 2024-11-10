from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import CASCADE

from common.models import BaseModel


class Category(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return f"Manufacturer:{self.name}\nAddress:{self.address}"


class Product(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=512, null=True, blank=True)
    price = models.FloatField(default=0)
    amount = models.IntegerField(default=1)
    category = models.ManyToManyField("products.Category",)
    manufacturer = models.ForeignKey("products.Manufacturer", on_delete=CASCADE)

    def __str__(self):
        return f"Product:{self.name}\nPrice:{self.price}\nManufacturer:{self.manufacturer.name}"


class Basket(models.Model):
    products = models.ManyToManyField("products.Product",)
    user = models.ForeignKey(get_user_model(), related_name="users_basket", on_delete=CASCADE)
    total_price = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.name}\nTotal price:{self.total_price}"
