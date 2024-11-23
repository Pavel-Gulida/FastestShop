from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from products.models import Product


class ListProducts(ListView):
    template_name = "products_list.html"
    queryset = Product.objects.all()


class CreateProduct(CreateView):
    template_name = "create.html"
    model = Product
    success_url = reverse_lazy("products:products_list")
    fields = ["name", "price", "category", "manufacturer"]


class UpdateProduct(UpdateView):
    template_name = "update.html"
    queryset = Product.objects.all()
    success_url = reverse_lazy("products:products_list")
    fields = ["name", "price", "category", "manufacturer"]


class DeleteProducts(DeleteView):
    template_name = "delete.html"
    queryset = Product.objects.all()
    success_url = reverse_lazy("products:products_list")
