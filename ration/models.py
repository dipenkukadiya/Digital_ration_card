from django.db import models
from django.forms import ValidationError
import datetime


class registerdb(models.Model):
    userselection =models.CharField(max_length=100)
    rationbooktype = models.CharField(max_length=100)
    sel = models.CharField(max_length=100)
    firstname= models.CharField(max_length=100)
    lastname= models.CharField(max_length=100)
    emailid= models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    contactno= models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    taluka = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pincode = models.CharField(max_length=6)
    address = models.CharField(max_length=100)
    shopno = models.CharField(max_length=100)
    shopaddress= models.CharField(max_length=100)
    aadharcard = models.CharField(max_length=100)
    passbook = models.CharField(max_length=100)
    income = models.CharField(max_length=100)
    residential = models.CharField(max_length=100)
    cast = models.CharField(max_length=100)
    bank = models.CharField(max_length=100)
    gas = models.CharField(max_length=100)
    electricity = models.CharField(max_length=100)
    password = models.CharField(max_length=8)
    credential = models.CharField(max_length=100)

    
class logindb(models.Model): 
    rationcardno = models.CharField(max_length=4)
    licenseno = models.CharField(max_length=4)
    emailidd= models.CharField(max_length=100)  
    passwordd = models.CharField(max_length=8)  

class familydb(models.Model):
    aadhaar =models.CharField(primary_key=True, max_length=100)
    f_name = models.CharField(max_length=12)
    age = models.CharField(max_length=12)
    gender = models.CharField(max_length=100)  
    relation = models.CharField(max_length=100) 
    uid = models.CharField(max_length=100)   

    def __str__(self):
        return self.uid

class rationdb(models.Model):
    ration_key = models.AutoField(primary_key=True)
    aadharnoo =models.CharField(max_length=100)
    datee= models.CharField(max_length=100 )
    otp  = models.CharField(max_length=4 ,default=0)
    serial = models.CharField(max_length=10)  
    product = models.CharField(max_length=100) 
    price= models.CharField(max_length=100)   
    bill = models.CharField(max_length=10)
    weight = models.CharField(max_length=100)              
    rationn = models.CharField(max_length=100)


class tokondb(models.Model):
    id = models.AutoField(primary_key=True)
    adharno = models.CharField(max_length=100)
    serial = models.CharField(max_length=10)
    product = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    weight = models.CharField(max_length=100)
    tokon_num = models.CharField(max_length=10)
  
class pricedb(models.Model):
    def sa(value):
            if value < datetime.date.today():
                raise ValidationError("The date cannot be in the past!")
            return value
    date = models.DateField(max_length=100, validators=[sa])
    sugar = models.CharField(max_length=100)
    oil = models.CharField(max_length=100)
    corn = models.CharField(max_length=100)
    wheat= models.CharField(max_length=100)
    rice = models.CharField(max_length=100)
    salt = models.CharField(max_length=100)
    dal = models.CharField(max_length=100)
    
class pricebpl(models.Model):
   
    sugar = models.CharField(max_length=100)
    oil = models.CharField(max_length=100)
    corn = models.CharField(max_length=100)
    wheat= models.CharField(max_length=100)
    rice = models.CharField(max_length=100)
    salt = models.CharField(max_length=100)
    dal = models.CharField(max_length=100)
class feedbackdb(models.Model):

    ee = models.CharField(max_length=100)
    complain = models.CharField(max_length=500)   