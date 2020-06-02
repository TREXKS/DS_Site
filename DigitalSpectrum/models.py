from django.db import models

# Create your models here.

class Category(models.Model):
    Category = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.Category}"

class Sensor(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    function = models.CharField(max_length=200)
    model_number =  models.CharField(max_length=64)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    size =  models.CharField(max_length=64)
    weight =  models.CharField(max_length=64)
    warrenty =  models.CharField(max_length=64)
    manufacturer =  models.CharField(max_length=64)
    def __str__(self):
        return f"{self.name} - ${self.price} "


class Unit(models.Model):
    name = models.CharField(max_length=64)
    sensor = models.ManyToManyField(Sensor, blank=True, related_name="units")

    def __str__(self):
        return f"{self.name} - {self.sensor} "


class System(models.Model):
    name = models.CharField(max_length=64)
    units = models.ManyToManyField(Unit, blank=True, related_name="system_pack")

    def __str__(self):
        return f"{self.name} - {self.units} "


class Crop(models.Model):
    name = models.CharField(max_length=64)
    type = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name} - {self.type} "


class Cart(models.Model):
    cart_item = models.ManyToManyField(Sensor, blank=True, related_name="cart_item")
    quantity = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.cart_item}"

class Checkout(models.Model):
    cart = models.ManyToManyField(Cart, blank=True, related_name="checked_items")
    total = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return f" {self.timestamp}"
