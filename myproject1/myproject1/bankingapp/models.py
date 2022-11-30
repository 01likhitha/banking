from django.db import models
# from django.contrib.auth.forms import UserCreationForm
# from django import forms
# from django.contrib.auth.models import User
# # Create your models here.
# class District(models.Model):
#     name=models.CharField(max_length=40)

#     def __str__(self):
#         return self.name

# class Branches(models.Model):
#     district=models.ForeignKey(District,on_delete=models.CASCADE)
#     name=models.CharField(max_length=40)

#     def __str__(self):
#         return self.name

# class Member(models.Model):
#     name = models.CharField(max_length=40)
#     dob=models.DateTimeField(max_length=40)
#     email=models.TextField(max_length=40)
#     number=models.TextField(max_length=40)
#     address=models.TextField(max_length=40)
#     district=models.ForeignKey(District,on_delete=models.SET_NULL,blank=True,null=True)
#     branches = models.ForeignKey(Branches, on_delete=models.SET_NULL, blank=True, null=True)

#     def __str__(self):
#         return self.name

class Uuser(models.Model):
    name = models.CharField(max_length=45,)
    public_repos = models.CharField(max_length=45,)

    
    def __str__(self):
        return self.name

class Registration(models.Model):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=20)
