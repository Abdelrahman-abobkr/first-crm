from django.contrib import admin
from .models import *
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ["user", "phone", "age", "img_tag", "img"]

class ProductAdmin(admin.ModelAdmin):
    list_filter = ["name", 'price']

    list_display = ["name", 'price']

class OrderAdmin(admin.ModelAdmin):
    list_filter = ['customer','product','status',]

    list_displa = ['customer','product','status',]

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)


admin.site.site_title = "CRM Admin"
admin.site.site_header = "CRM Admin Site"
admin.site.index_title = "CRM Adminstration"
admin.site.site_url = "/"