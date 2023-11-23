from django.contrib import admin
from .models import Category, Wrapper, IceCream, Topping

# Register your models here.
admin.site.register(Category)
admin.site.register(Wrapper)
admin.site.register(IceCream)
admin.site.register(Topping)
    