from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class City(models.Model):
    name = models.TextField()

    def __str__(self):
        return f"{self.name}"

class District(models.Model):
    name = models.TextField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}, {self.city}"

class Shop(models.Model):
    name = models.TextField()
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    opening_time = models.TimeField()
    close_time =  models.TimeField()

    def __str__(self):
        return f"{self.name}. {self.opening_time}-{self.close_time}. {self.address}, {self.district}"

class Category(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    name = models.TextField()

    def __str__(self):
        return f"{self.shop}. {self.name}"

class Product(models.Model):
    name = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.category}. {self.name}. {self.price}Р"

class Client(models.Model):
    name = models.TextField()
    surname = models.TextField()
    phone_num = models.CharField(max_length=11)
    address = models.CharField(max_length=255)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.surname}. {self.phone_num}. {self.address}, {self.district}"

class Transport(models.Model):
    number = models.CharField(max_length=11)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.number}. {self.city}"

class Courier(models.Model):
    name = models.TextField()
    surname = models.TextField()
    phone_num = models.CharField(max_length=11)
    transport = models.ForeignKey(Transport, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.surname}. {self.phone_num}. {self.transport}"
   

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    beg_time = models.DateTimeField()
    end_time = models.DateTimeField()
    price = models.CharField(max_length=11)
    done = models.BooleanField()
    order_list = models.ManyToManyField("Product", blank=True)
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE)

    def __str__(self):
        return f"Клиент:{self.client}. Курьер:{self.courier}. Время:{self.beg_time}-{self.end_time}. Цена: {self.price}Р. Отметка о выполнении заказа: {self.done}"


