from contextlib import _AsyncGeneratorContextManager
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField(unique=True,max_length=40)
    password = models.CharField(max_length=30)
    role = models.CharField(max_length=10)
    otp = models.IntegerField(default=456)
    is_verify = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self) -> str:
        return self.email

class Doctor(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    qualification = models.CharField(max_length=50,blank=True,null=True)
    specification = models.CharField(max_length=50,blank=True,null=True)
    available_time = models.CharField(max_length=50,blank=True,null=True)
    experiance = models.CharField(max_length=50,blank=True,null=True)
    clinic_name = models.CharField(max_length=50,blank=True,null=True)
    clinic_city = models.CharField(max_length=50,blank=True,null=True)
    clinic_address = models.TextField(blank=True,null=True)
    mobile = models.CharField(max_length=20,blank=True,null=True)
    pic = models.FileField(upload_to = "media/images", default = "media/default_doc.png")

    def __str__(self) -> str:
        return self.firstname

    
class Patient(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    age = models.CharField(max_length=10, blank=True,null=True)
    gender = models.CharField(max_length=10, blank=True,null=True)
    birthdate = models.CharField(max_length=10, blank=True,null=True)
    blood_group = models.CharField(max_length=10, blank=True,null=True)
    height = models.CharField(max_length=10, blank=True,null=True)
    weight = models.CharField(max_length=10, blank=True,null=True)
    address = models.TextField(blank=True,null=True)
    mobile = models.CharField(max_length=10, blank=True,null=True)
    pic = models.FileField(upload_to = "media/images", default = "media/default_doc.png")

    def __str__(self) -> str:
        return self.firstname
