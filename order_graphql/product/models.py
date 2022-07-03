from django.db import models


class Product(models.Model):
    category = models.CharField(max_length=200, null=True)
    brand = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200, null=True)
    price = models.IntegerField(null=True)
    quantity = models.IntegerField(null=True)
    imageurl = models.ImageField(upload_to ='static')

    def __str__(self):
        return str(self.id)


class Order(models.Model):
    timestamp = models.DateTimeField(null=True)
    placed = models.BooleanField(default=False)
    total_price = models.IntegerField(null=True)
    total_quantity = models.IntegerField(null=True)
    products = models.ManyToManyField(Product)