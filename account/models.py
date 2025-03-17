from django.db import models
from django.contrib.auth.models import User

# Create your models here.

userType=[
    ('Admin','Admin'),
    ('Patiant','Patiant'),
    ('Donar','Donar')
]

class Registration(models.Model):
    usertype = models.CharField(choices=userType,null=True,blank=True,max_length=100,default='Patiant')
    user = models.OneToOneField(User, on_delete = models.CASCADE,null=True,blank=True)
    mobile = models.CharField(max_length=12,null=True,blank=True)
    picture = models.URLField(max_length=300,null=True,blank=True)
    created = models.DateTimeField(null=True,blank=True,auto_now_add=True)
    def __str__(self):
        return self.user.username
    