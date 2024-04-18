from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from .managers import CustomManager

# Create your models here.      
class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=30, null=True)
    middle_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    username = models.CharField(max_length=30, unique=True, null=True)
    email = models.EmailField(max_length=100, unique=True, null=True)
    tel_number = models.IntegerField( null=True)
    Date_Registered = models.DateTimeField(auto_now_add = True)
    last_login =  models.DateTimeField(auto_now = True)
    gender = (
              ( 'M', 'Male'),
              ('F', 'Female'),
              )
    Gender = models.CharField(max_length=1, blank=True, choices=gender)
    
    def display_gender(self):
       return ','.join(gender.name for gender in self.gender[:2])
    display_gender.short_description = 'Gender'
    #permissions
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    objects = CustomManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'tel_number']
    def has_perm(self, perm, obj=None):
           return self.is_admin

    def has_module_perms(self, add_label):
       return True

 
class Profile(models.Model):
    #Address Details
    Holder = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    postal_address = models.CharField(max_length=20, null=True)
    house_address = models.CharField(max_length=20, null=True)
    City = models.CharField(max_length=50, null=True)
    region = models.CharField(max_length=50, null=True)
    date_of_birth = models.DateField(null = True, blank = True)
    country = models.CharField(max_length=50, null=True)
    #Biometrics
    profile_picture = models.ImageField(upload_to='images/profilepictures/') 
    
class LoginModel(models.Model):
       email = models.EmailField()
       password= models.CharField(max_length=150)
   

       
       
              