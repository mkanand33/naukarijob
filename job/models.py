from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserProfile(AbstractUser):

     user_mobile = models.IntegerField( null=True)
     user_bank_name=models.CharField(max_length=100,null=True)
     user_bank_account_number=models.CharField(max_length=50, null=True)
     user_bank_ifsc_code = models.CharField(max_length=30,null=True)
     user_byt_balance = models.IntegerField( null=True)