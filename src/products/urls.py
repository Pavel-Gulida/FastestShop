from django.urls import path

from products.views import (create_categories, create_manufacturers,
                            create_products)

app_name = "products"

urlpatterns = [
    path("create_categories/", create_categories, name="create_categories"),
    path("create_manufacturers/", create_manufacturers, name="create_manufacturers"),
    path("create_products/", create_products, name="create_products"),
]
