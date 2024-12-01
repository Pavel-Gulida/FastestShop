from django.db.models import Q
from django.views.generic import ListView

from products.models import Category, Product, Basket


class IndexView(ListView):
    model = Product
    template_name = "index.html"

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        category = self.request.GET.get("category")

        if (query is None and category):
            object_list = super().get_queryset().filter(category=category)
        elif (query is None):
            object_list = super().get_queryset()
        else:
            object_list = Product.objects.filter(
                Q(name__icontains=query) | Q(description__icontains=query)
            )

        product_id = self.request.GET.get("p")
        user = self.request.user
        if(product_id is not None):
            user_basket = Basket.objects.get(user=user)
            user_basket.products.add(product_id)

        return {"products": object_list, "categories": Category.objects.all()}
