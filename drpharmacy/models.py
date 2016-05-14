'''
Created on Aug 2, 2012

@author: hossain
'''
from django.db import models


class Company(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID')
    name = models.CharField(max_length=135, blank=True)
    address = models.CharField(max_length=135, blank=True)
    region = models.CharField(max_length=135, blank=True)
    state = models.CharField(max_length=135, blank=True)
    country = models.CharField(max_length=135, blank=True)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        db_table = u'location'



class Product(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID')
    company = models.ForeignKey(Company, related_name='company')
    
    name = models.CharField(max_length=500, blank=True)
    
    pcode = models.CharField(max_length=500, blank=True)
    dosage_form = models.CharField(max_length=500, blank=True)
    manufacturer = models.CharField(max_length=500, blank=True)
    ingridient1 = models.CharField(max_length=500, blank=True)
    ingridient2 = models.CharField(max_length=500, blank=True)
    ingridient3 = models.CharField(max_length=500, blank=True)
    pclass = models.CharField(max_length=500, blank=True)
    pbrand = models.CharField(max_length=500, blank=True)
    packet_size = models.CharField(max_length=500, blank=True)
    strength = models.CharField(max_length=500, blank=True)
    dose_type = models.CharField(max_length=500, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    
    #buy_price = CurrencyField(decimal_places=2,max_digits=10, null=True, blank=True)
    
    isenabled = models.IntegerField(null=True, blank=True)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        db_table = u'products'




'''
class ProductStat(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID')
    machine = models.ForeignKey(Machines, related_name='machines')
    product = models.ForeignKey(Products, related_name='sold_products')
    quantity = models.IntegerField(null=True, blank=True)
    sold_price = models.DecimalField(decimal_places=2, max_digits=5)
    date = models.DateTimeField(null=True, blank=True)
    
    def __unicode__(self):
        return str(self.id)
    
    class Meta:
        db_table = u'sales'
'''

