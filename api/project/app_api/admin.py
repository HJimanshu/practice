from django.contrib import admin
from app_api.models import *
# Register your models here.
class Companyadmin(admin.ModelAdmin):
    list_display=['name','location','about']
    list_filter=['name']
class Employeeadmin(admin.ModelAdmin):
    list_display=['name','email','address','position']
    list_filter=['position']
    
admin.site.register(Company1,Companyadmin)
admin.site.register(Employee1,Employeeadmin)