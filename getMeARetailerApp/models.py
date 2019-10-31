from django.db import models


# Create your models here.
class Provider(models.Model):
    title = models.CharField(max_length=25)
    parent = models.CharField(max_length=25)
    founded = models.IntegerField()
    focus_category = models.CharField(max_length=25)
    rating = models.IntegerField()

    def __str__(self):
        return self.title + ":" + self.parent + ":" + str(self.founded) + ":" + str(self.rating)


class Product(models.Model):
    title = models.CharField(max_length=25)
    brand = models.CharField(max_length=25)
    specs = models.CharField(max_length=100)
    price = models.FloatField()
    site = models.ForeignKey(Provider, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ":" + self.brand + ":" + self.site.title + ":" + str(self.price)


class Logistic(Provider):
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    delivery_time = models.IntegerField()

    def __str__(self):
        return self.title + ":" + self.item.title + ":" + self.item.site.title \
               + ":" + str(self.rating) + ":" + str(self.delivery_time)
