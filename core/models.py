from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Shop(models.Model):
    name = models.TextField()
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    opening_time = models.TimeField()
    close_time =  models.TimeField()

class Category(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    name = models.TextField()

class Product(models.Model):
    name = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField()

class District(models.Model):
    name = models.TextField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)

class Client(models.Model):
    name = models.TextField()
    surname = models.TextField()
    phone_num = models.CharField(max_length=11)
    address = models.CharField(max_length=255)
    district = models.ForeignKey(District)

class City(models.Model):
    name = models.TextField()

class Order(models.Model):
    client = models.ForeignKey(Client)
    beg_time = models.DateTimeField()
    end_time = models.DateTimeField()
    price = models.CharField(max_length=11)
    done = models.BooleanField()
    order_list = models.ManyToManyField("Product", blank=True)
    courier = models.ForeignKey(Courier)
    transport = models.ForeignKey(Transport)

class Courier(models.Model):
    client = models.ForeignKey(Client)
    beg_time = models.DateTimeField()
    end_time = models.DateTimeField()
    price = models.CharField(max_length=11)
    done = models.BooleanField()
    order_list = models.ManyToManyField("Product", blank=True)
    courier = models.ForeignKey(Courier)
    transport = models.ForeignKey(Transport)

class Transport(models.Model):
    number = models.CharField(max_length=11)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

