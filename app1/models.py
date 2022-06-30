from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.contrib.auth.models import User


class crtcompony(models.Model):
    componyname = models.CharField(max_length=50)
    mailingname = models.CharField (max_length=50)
    address = models.CharField (max_length=50)
    state = models.CharField (max_length=50)
    country = models.CharField (max_length=50)
    pincode = models.CharField (max_length=10)
    telphone = models.CharField(max_length=10)
    mobile = models.CharField(max_length=10)
    fax = models.CharField(max_length=10)
    email=models.EmailField()
    website=models.CharField(max_length=100)
    fyearbgn=models.DateField()
    booksbgn=models.DateField()
    curncysymbl=models.CharField(max_length=10)
    crncyname=models.CharField(max_length=10)
    
class GroupModel(models.Model):
    name = models.CharField(max_length=225)
    alias = models.CharField(max_length=225,null=True)
    under = models.CharField(max_length=225)
    gp_behaves_like_sub_ledger = models.CharField(max_length=225)
    nett_debit_credit_bal_reporting = models.CharField(max_length=225)
    used_for_calculation = models.CharField(max_length=225)
    method_to_allocate_usd_purchase = models.CharField(max_length=225,null=True,blank=True)

    def __str__(self):
        return self.name

#class group(models.Model):

#// class LedgerModel(models.Model):
    #cid = models.ForeignKey(
     #   CompanyModel, on_delete=models.CASCADE, null=True, blank=True)
    #ledger_name = models.CharField(max_length=225)
    #ledger_alias = models.CharField(max_length=225)

    #group = models.ForeignKey(
      #  GroupModel, on_delete=models.CASCADE, null=True, blank=True)
    #ledger_opening_bal = models.CharField(max_length=225)
    #ledger_type = models.CharField(max_length=225)
    #type_of_duty = models.CharField(max_length=225)
    #percent_of_calculation = models.CharField(max_length=225)
    #maintain_bal_bill = models.CharField(max_length=225)
   # credit_days_during_voucher_entry = models.CharField(max_length=225)
    #default_cr_peroid = models.CharField(max_length=225)
    #provide_banking_details = models.BooleanField()

    #def __str__(self):
        #return self.ledger_name 

class CreateCurrency(models.Model):
    symbol =models.CharField(max_length=225)
    formal_name=models.CharField(max_length=225)
    ISO_code=models.CharField(max_length=225)
    decimal_places= models.CharField(max_length=225,default=2)
    show_in_millions =  models.CharField(max_length=225)
    suffix_to_amount=  models.CharField(max_length=225)
    space_symbol_amount = models.CharField(max_length=225)
    word_after_decimal = models.CharField(max_length=225)
    decimal_no_in_words = models.CharField(max_length=225)
    flag= models.CharField(max_length=225,default=0)