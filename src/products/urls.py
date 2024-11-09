from django.urls import path

from products.views import (CreateProduct, DeleteProducts, ListProducts,
                            UpdateProduct)

app_name = "products"

urlpatterns = [
    path("", ListProducts.as_view(), name="products_list"),
    path("create/", CreateProduct.as_view(), name="create_product"),
    path("update/<int:pk>/", UpdateProduct.as_view(), name="update_product"),
    path("delete/<int:pk>/", DeleteProducts.as_view(), name="delete_product"),
]
