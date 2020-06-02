from django.contrib import admin

# Register your models here.
from .models import Sensor, Category, Cart, Checkout, Unit, System, Crop
#
# # Register your models here.
admin.site.register(Sensor)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(Checkout)
admin.site.register(Unit)
admin.site.register(System)
admin.site.register(Crop)
