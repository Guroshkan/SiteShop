from django.contrib import admin
from .models import Product, Type, Price


admin.site.register(Type)
admin.site.register(Price)
admin.site.register(Product)
