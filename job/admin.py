from django.contrib import admin

# Register your models here.
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
