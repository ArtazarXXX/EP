from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from core.models import Shop, Category, Product, District, Client, City, Order, Courier, Transport

class ShopResource(resources.ModelResource):
    class Meta:
        model = Shop
        skip_unchanged = True
        report_skipped = False
@admin.register(Shop)
class ShopAdmin(ImportExportModelAdmin):
    list_display = ("name", "opening_time", "close_time", "address", "district")

    list_filter = ("district", )

    search_fields = ("name__startswith", "address__startswith")

    resource_class = ShopResource


class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category
        skip_unchanged = True
        report_skipped = False
@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ("name", "shop")

    list_filter = ("shop", )

    search_fields = ("name__startswith", )

    resource_class = CategoryResource

class ProductResource(resources.ModelResource):
    class Meta:
        model = Product
        skip_unchanged = True
        report_skipped = False
@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = ("name", "category", "price")

    list_filter = ("category", )

    search_fields = ("name__startswith", )

    resource_class = ProductResource


class DistrictResource(resources.ModelResource):
    class Meta:
        model = District
        skip_unchanged = True
        report_skipped = False
@admin.register(District)
class DistrictAdmin(ImportExportModelAdmin):
    list_display = ("name", "city")

    list_filter = ("city", )

    search_fields = ("name__startswith", )

    resource_class = DistrictResource

class ClientResource(resources.ModelResource):
    class Meta:
        model = Client
        skip_unchanged = True
        report_skipped = False
@admin.register(Client)
class ClientAdmin(ImportExportModelAdmin):
    list_display = ("name", "surname", "phone_num", "address", "district")

    list_filter = ("district", )

    search_fields = ("name__startswith", "surname__startswith", "phone_num__startswith", "address__startswith")

    resource_class = Client

class CityResource(resources.ModelResource):
    class Meta:
        model = City
        skip_unchanged = True
        report_skipped = False
@admin.register(City)
class CityAdmin(ImportExportModelAdmin):
    resource_class = CityResource

class OrderResource(resources.ModelResource):
    class Meta:
        model = Order
        skip_unchanged = True
        report_skipped = False
@admin.register(Order)
class OrderAdmin(ImportExportModelAdmin):
    list_display = ("client", "courier", "beg_time", "end_time", "price", "done")

    list_filter = ("done", )

    search_fields = ("client__startswith", "courier__startswith", "price__startswith")

    resource_class = OrderResource

class CourierResource(resources.ModelResource):
    class Meta:
        model = Courier
        skip_unchanged = True
        report_skipped = False
@admin.register(Courier)
class CourierAdmin(ImportExportModelAdmin):
    list_display = ("name", "surname", "phone_num", "transport")

    search_fields = ("name__startswith", "surname__startswith", "phone_num__startswith", "transport__startswith")

    resource_class = CourierResource

class TransportResource(resources.ModelResource):
    class Meta:
        model = Transport
        skip_unchanged = True
        report_skipped = False
@admin.register(Transport)
class TransportAdmin(ImportExportModelAdmin):
    list_display = ("number", "city")

    list_filter = ("city", )

    search_fields = ("number__startswith", )

    resource_class = TransportResource