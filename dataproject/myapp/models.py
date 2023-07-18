from django.db import models
from django.contrib import admin
# Create your models here.
class student (models.Model):
    referencenumber=models.CharField(primary_key=True,max_length=20,help_text="referencenumber")
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField()
    phonenumber=models.IntegerField()


class StudentAdmin(admin.ModelAdmin):
    list_display=('referencenumber','name','age','email','phonenumber')