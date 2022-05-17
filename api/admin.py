from .models import *
from django.contrib import admin


class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "first_name", "last_name", "email"]


class CarBrandAdmin(admin.ModelAdmin):
    list_display = ["name", "is_deleted", "deleted_at"]


admin.site.register(User, UserAdmin)
admin.site.register(CarBrand, CarBrandAdmin)
admin.site.register(CarModel)
admin.site.register(UserCar)
admin.site.register(Car)
