from django.contrib import admin
from .models import *

class hotelAdmin(admin.ModelAdmin):
    list_display = ['hotel_name','hotel_price','hotel_discription']

admin.site.register(data,hotelAdmin)