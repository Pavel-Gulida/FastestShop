from celery import shared_task

from products.models import Category, Manufacturer, Product


@shared_task
def create_fake_categories():
    Category.generate_instances(10)


@shared_task
def create_fake_manufacturers():
    Manufacturer.generate_instances(50)


@shared_task
def create_fake_products():
    Product.generate_instances(100)
