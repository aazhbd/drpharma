'''
Created on Aug 3, 2012

@author: hossain
'''
from drpharmacy.models import *
from django.contrib import admin

class ProductAdmin(admin.ModelAdmin):
    pass

class CompanyAdmin(admin.ModelAdmin):
    pass

admin.site.register(Product, ProductAdmin)
admin.site.register(Company, CompanyAdmin)
