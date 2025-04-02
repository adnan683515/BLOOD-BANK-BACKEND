from django.contrib import admin
from django.template.loader import render_to_string
from django.core.mail import  EmailMultiAlternatives
from .models import DonateBlood,BloodRequest
# Register your models here.


admin.site.register(DonateBlood)
admin.site.register(BloodRequest)