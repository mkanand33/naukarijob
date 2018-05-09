from django.contrib import admin
from django.contrib import admin
from django.conf import settings
#from .models import User

# Register your models here.
#admin.site.register(User)

# Register your models here.
'''
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import UserProfile

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'userprofile'

class UserProfileAdmin(admin.ModelAdmin):
    can_delete = False
    verbose_name_plural = 'userprofile'

admin.site.register(UserProfile, UserProfileAdmin)
'''
from .models import *



class JobListAdmin(admin.ModelAdmin):
	list_display = ['title','description']

class UserListAdmin(admin.ModelAdmin):
	user_display = ['username','password']	


admin.site.register(job_listing, JobListAdmin)
admin.site.register(user_detail, UserListAdmin)
