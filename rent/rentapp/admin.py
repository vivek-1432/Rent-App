from django.contrib import admin
from rentapp.models import prod

#Register your models here.

class prodName(admin.ModelAdmin):
    list_display = ['name', 'product', 'price', 'date', 'till', 'image']

admin.site.register(prod, prodName)