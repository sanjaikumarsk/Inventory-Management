from django.db import models

# Create your models here.
class User(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100,null=False)
    password = models.CharField(max_length=200,null=False)
    emailID = models.CharField(max_length=200)
    mobileno = models.CharField(max_length=30)
    shopname = models.CharField(max_length=200)
    usertimezone = models.CharField(max_length=100)
    createdat = models.DateTimeField()
    createdby = models.IntegerField()
    modifiedat = models.DateTimeField()
    modifiedby = models.IntegerField()
    status = models.BooleanField(default=True)

class UserLoginTime(models.Model):
    logintimeid = models.AutoField(primary_key=True)
    userid = models.IntegerField()
    logintime = models.DateTimeField()

class ProductDetails(models.Model):
    productid = models.AutoField(primary_key=True)
    productname = models.CharField(max_length=255)
    productdescription = models.CharField(max_length=500,default='')
    productcategory = models.CharField(max_length=100)
    barcode = models.CharField(max_length=200,default='')
    isownproduct = models.BooleanField(default=False)
    supplierid = models.IntegerField()
    userid = models.IntegerField()
    createdat = models.DateTimeField()
    createdby = models.IntegerField()
    modifiedat = models.DateTimeField()
    modifiedby = models.IntegerField()
    status = models.BooleanField(default=True)

class ProductRateDetails(models.Model):
    prodrateid = models.AutoField(primary_key=True)
    productid = models.IntegerField()
    rate = models.DecimalField(max_digits=None)
    createdat = models.DateTimeField()
    createdby = models.IntegerField()
    modifiedat = models.DateTimeField()
    modifiedby = models.IntegerField()
    status = models.BooleanField(default=True)