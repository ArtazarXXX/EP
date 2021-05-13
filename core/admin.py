from django.contrib import admin

from core.models import Shop, Category, Product, District, Client, City, Order, Courier, Transport

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    pass

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass

@admin.register(Courier)
class CourierAdmin(admin.ModelAdmin):
    pass

@admin.register(Transport)
class TransportAdmin(admin.ModelAdmin):
    pass