from products.models import Product,Category,Manufacturer

def sample_product(**params):
    default = {
               "name":"TestProduct",
               "description":"test",
               "price":9999.99,
               "amount":1,
               "category": [Category.objects.get_or_create(name="TestCategory")[0]],
               "manufacturer":Manufacturer.objects.get_or_create(name="TestManufacturer")[0]
               }
    default.update(params)

    return Product.objects.create( **default)
