from django.db import models

from django.db import models
#from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

# Create your models here.
#from django.db import models
#from django.contrib.auth.models import User
#from django.contrib.auth.models import AbstractUser
# Create your models here.
'''
class UserProfile(AbstractUser):

     user_mobile = models.IntegerField( null=True)
     user_bank_name=models.CharField(max_length=100,null=True)
     user_bank_account_number=models.CharField(max_length=50, null=True)
     user_bank_ifsc_code = models.CharField(max_length=30,null=True)
     user_byt_balance = models.IntegerField( null=True)

    '''

'''
class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        """
        Creates and saves a User with the given username and password.
        """
        if not username:
            raise ValueError('Users must have an username address')

        user = self.model(
            username=self.normalize_username(username),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, username, password):
        """
        Creates and saves a staff user with the given username and password.
        """
        user = self.create_user(
            username,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        """
        Creates and saves a superuser with the given username and password.
        """
        user = self.create_user(
            username,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user  





class User(AbstractBaseUser):
    username = models.CharField(
        verbose_name='username address',
        max_length=255,
        unique=True,
    )
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser
    # notice the absence of a "Password field", that's built in.

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [] # username & Password are required by default.

    def get_full_name(self):
        # The user is identified by their username address
        return self.username

    def get_short_name(self):
        # The user is identified by their username address
        return self.username

    def __str__(self):              # __unicode__ on Python 2
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active


'''


class job_listing(models.Model):
	title = models.TextField(null=True, blank=True)     
	description = models.TextField(null=True, blank=True) 




class user_detail(models.Model):
	username = models.CharField(max_length = 30, null=True, blank=True)
	password = models.CharField(max_length = 30, null=True, blank=True)

	def __str__(self):
		return self.username

	def __str__(self):
		return self.password   
