from .models import *
from django.contrib import admin

class CarModelAdmin(admin.ModelAdmin):
    list_display = ["car_brand", "name"]

class UserCarAdmin(admin.ModelAdmin):
    list_display = ["user", "car_brand", "car_model", "odometer"]

class CarAdmin(admin.ModelAdmin):
    list_display = ["user", "car_brand"]

admin.site.register(User)
admin.site.register(CarBrand)
admin.site.register(CarModel, CarModelAdmin)
admin.site.register(UserCar, UserCarAdmin)
admin.site.register(Car)
