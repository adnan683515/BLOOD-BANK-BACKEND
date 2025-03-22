from django.contrib import admin
from .models import DonateBlood,BloodRequest
# Register your models here.
admin.site.register(DonateBlood)
admin.site.register(BloodRequest)