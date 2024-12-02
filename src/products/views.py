# from django.db.models import Q
# from django.urls import reverse_lazy
# from django.views.generic import CreateView, DeleteView, ListView, UpdateView
#
from django.http import HttpRequest, HttpResponse

from products.tasks import (create_fake_categories, create_fake_manufacturers,
                            create_fake_products)


def create_categories(request: HttpRequest) -> HttpResponse:
    create_fake_categories.delay()
    return HttpResponse("Task create categories is started")


def create_manufacturers(request: HttpRequest) -> HttpResponse:
    create_fake_manufacturers.delay()
    return HttpResponse("Task create manufacturers is started")


def create_products(request: HttpRequest) -> HttpResponse:
    create_fake_products.delay()
    return HttpResponse("Task create products is started")


# class ListProducts(ListView):
#     model = Product
#     template_name = "products_list.html"
#
#     def get_queryset(self):  # new
#         query = self.request.GET.get("q")
#         if (query is None):
#             object_list = super().get_queryset()
#         else:
#             object_list = Product.objects.filter(
#                 Q(name__icontains=query) | Q(description__icontains=query)
#             )
#         return object_list
#
#
# class CreateProduct(CreateView):
#     template_name = "create.html"
#     model = Product
#     success_url = reverse_lazy("products:products_list")
#     fields = ["name", "price", "category", "manufacturer"]
#
#
# class UpdateProduct(UpdateView):
#     template_name = "update.html"
#     queryset = Product.objects.all()
#     success_url = reverse_lazy("products:products_list")
#     fields = ["name", "price", "category", "manufacturer"]
#
#
# class DeleteProducts(DeleteView):
#     template_name = "delete.html"
#     queryset = Product.objects.all()
#     success_url = reverse_lazy("products:products_list")
