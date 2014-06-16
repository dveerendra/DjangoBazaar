from django.contrib import admin
from shop.models import Item, UserInfo
# Register your models here.

class shop(admin.ModelAdmin):
    admin.site.register(UserInfo)
    admin.site.register(Item)