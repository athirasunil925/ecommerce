from django.contrib import admin
from . models import Category,Product
# Register your models here.
class Category_admin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category,Category_admin)
class Product_admin(admin.ModelAdmin):
    list_display = ['name','price','stock','available','created','updated']
    list_editable = ['price','stock','available']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Product,Product_admin)