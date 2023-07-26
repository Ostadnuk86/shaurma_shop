from django.contrib import admin

from django.contrib import admin
from .models import *

admin.site.register(Addresses)
admin.site.register(Clients)
admin.site.register(PaymentMethod)
admin.site.register(Orders)
admin.site.register(OrderStatus)
admin.site.register(Items)
admin.site.register(ItemsOrder)
admin.site.register(CategoryItems)
