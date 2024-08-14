from django.contrib import admin
from app_api.models import *
# Register your models here.
class companyadmin(admin.ModelAdmin):
    list_display=('name', 'about','type' )
    search_fields=('name',)
class employeesadmin(admin.ModelAdmin):
    list_display=('name', 'email','address' )
    list_filter=('company',)
admin.site.register(Company, companyadmin)
admin.site.register(Employee, employeesadmin)