from django.contrib import admin

from .models import Item, Item_type

# Register your models here.
admin.site.register(Item)
admin.site.register(Item_type)