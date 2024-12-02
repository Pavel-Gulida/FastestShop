import random

import faker_commerce
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import CASCADE
from faker import Faker


class Category(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    @classmethod
    def generate_instances(cls, count):
        faker = Faker()
        faker.add_provider(faker_commerce.Provider)
        for _ in range(count):
            category = Category(name=faker.ecommerce_category())
            category.save()

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=256, null=True, blank=True)

    @classmethod
    def generate_instances(cls, count):
        faker = Faker()
        for _ in range(count):
            manufacturer = Manufacturer(
                name=faker.company(),
                address=faker.address()
            )
            manufacturer.save()

    def __str__(self):
        return f"Manufacturer:{self.name}\nAddress:{self.address}"


class Product(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=512, null=True, blank=True)
    price = models.FloatField(default=0)
    amount = models.IntegerField(default=1)
    category = models.ManyToManyField("products.Category",)
    manufacturer = models.ForeignKey("products.Manufacturer", on_delete=CASCADE)

    @classmethod
    def generate_instances(cls, count):
        faker = Faker()
        faker.add_provider(faker_commerce.Provider)
        categories_id = list(Category.objects.values_list("id", flat=True))
        manufacturers_id = list(Manufacturer.objects.values_list("id", flat=True))
        for _ in range(count):
            product = Product(
                name=faker.ecommerce_name(),
                description=faker.text(500),
                price=faker.ecommerce_price(as_int=False),
                manufacturer=Manufacturer.objects.get(id=random.choice(manufacturers_id))
            )
            product.save()
            product.category.add(Category.objects.get(id=random.choice(categories_id)))

    def __str__(self):
        return f"Product:{self.name}\nPrice:{self.price}\nManufacturer:{self.manufacturer.name}"


class Basket(models.Model):
    products = models.ManyToManyField("products.Product",)
    user = models.ForeignKey(get_user_model(), related_name="users_basket", on_delete=CASCADE)
    total_price = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user}\nTotal price:{self.total_price}"
