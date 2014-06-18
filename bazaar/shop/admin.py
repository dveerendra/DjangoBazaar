from django.contrib import admin
from shop.models import MaterialItem, Tags, Comment, Ratings, ProviderOrganization
# Register your models here.

class shop(admin.ModelAdmin):
    admin.site.register(MaterialItem)
    admin.site.register(Tags)
    admin.site.register(Comment)
    admin.site.register(Ratings)
    admin.site.register(ProviderOrganization)