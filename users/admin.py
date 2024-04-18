from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class UserAccount(UserAdmin):
    list_display = ('email','first_name', 'middle_name', 'last_name', 'username', 'last_login', 'is_active',)
    readonly_fields = ('last_login', 'Date_Registered',)
    
    filter_horizontal = ()
    list_filter = ()
# makes password field readonly
    fieldsets = () 
    
admin.site.register(CustomUser, UserAccount)