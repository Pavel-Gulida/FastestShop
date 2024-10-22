from django.contrib import admin

from products.models import Basket, Category, Manufacturer, Product

admin.site.register([Basket, Product, Category, Manufacturer])
