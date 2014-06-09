from django.contrib import admin
from Bmodels.models import Item, UserInfo
# Register your models here.

class BmodelAdmin(admin.ModelAdmin):
    admin.site.register(UserInfo)
    admin.site.register(Item)