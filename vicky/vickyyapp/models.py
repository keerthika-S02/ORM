from django.db import models
from django.contrib import admin
class vehicle_DB(models.Model):
    vehicle_type=models.TextField()
    vehicle_no=models.CharField(max_length=15,primary_key=True)
    owner_phone_no=models.IntegerField()
    owner_address=models.TextField()
    owner_name=models.CharField(max_length=11)
    vehicle_brand=models.CharField(max_length=12)
    owner_email=models.EmailField()
class vehicle_DBAdmin(admin.ModelAdmin):
    list_display=["vehicle_type","vehicle_no","owner_phone_no","owner_address","owner_name","vehicle_brand","owner_email"]

