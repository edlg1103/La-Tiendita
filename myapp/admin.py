from django.contrib import admin
from .models import Product


admin.site.site_header="La Tiendita"
admin.site.site_title= "La Tiendita"
admin.site.index_title= "Administar"

class ProductAdmin(admin.ModelAdmin):
    list_display= ('name','price','desc')
    search_fields= ('name',)

admin.site.register(Product,ProductAdmin)