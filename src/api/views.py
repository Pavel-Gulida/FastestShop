from rest_framework.viewsets import ModelViewSet

from api.permissions import IsSuperUser
from api.serializers import ProductSerializer
from products.models import Product


class ProductViewSet(ModelViewSet):
    permission_classes = [IsSuperUser]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
