from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey



class Product(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=200)
    product = models.ForeignKey(Product, related_name='product', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Site(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Order(models.Model):
    product1 = models.ForeignKey(Product, related_name='product1', on_delete=models.CASCADE)
    product2 = models.ForeignKey(Product, related_name='product2', on_delete=models.CASCADE)
    site1 = models.ForeignKey(Site, related_name='site1', on_delete=models.CASCADE)
    site2 = models.ForeignKey(Site, related_name='site2', on_delete=models.CASCADE)
    quantity1 = models.PositiveIntegerField()
    quantity2 = models.PositiveIntegerField()
    type1 = models.ForeignKey(Type, related_name='type1', on_delete=models.CASCADE)
    type2 = models.ForeignKey(Type, related_name='type2', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
