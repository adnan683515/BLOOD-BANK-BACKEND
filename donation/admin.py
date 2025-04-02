from django.contrib import admin
from django.template.loader import render_to_string
from django.core.mail import  EmailMultiAlternatives
from .models import DonateBlood,BloodRequest
# Register your models here.


admin.site.register(DonateBlood)



class ModelAdminBloodRequest(admin.ModelAdmin):
    list_display  = ['user','numberOfBag','donateDate','place','mobile','status']
    

    def numberOfBag(self,obj):
        return obj.numberOfBag
    
    def donateDate(self,obj):
        return obj.donateDate
    
    def place(self,obj):
        return obj.place
    
    def email(self,obj):
        return obj.user.email
    
    
    

    def save_model(self, request, obj, form, change):
        obj.save()
        if obj.status == 'Accepted':
            mail_sub = 'Congress!!'
            email_body = render_to_string('sendReqEmail.html',{'user':obj.user,'DonateBlood':obj.DonateBlood})
            email = EmailMultiAlternatives(mail_sub,'',to=[obj.user.email])
            email.attach_alternative(email_body,'text/html')
            email.send()
            
    
admin.site.register(BloodRequest,ModelAdminBloodRequest)