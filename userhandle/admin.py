from django.contrib import admin
from .models import Booked, HandymanUser, Rate, ServiceOffering



admin.site.register(HandymanUser)
admin.site.register(Booked)
admin.site.register(ServiceOffering)
