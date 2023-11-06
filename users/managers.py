from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone



class CustomManager(BaseUserManager):
    use_in_migrations = True
       
    def _create_user(self, email, tel_number,username, password, **other_fields):
           values = [email, tel_number, username]
           #map the list in the required fields and the list in values above into a single dictionary
           field_value_map = dict(zip(self.model.REQUIRED_FIELDS, values)) 
           #Get both the key(fieldname) and the value
           for field_name, value in field_value_map.items():
              if not value:
                     #raise value error string the {fieldname} must be set
                     raise ValueError('The {} value must be set'.format(field_name))
              
           email = self.normalize_email(email)
           user = self.model(email=email, tel_number=tel_number, username=username, **other_fields)
           user.set_password(password)
           user.save(using=self._db)
           return user
           
    def create_superuser(self, email, tel_number, username, password=None, **other_fields):
           #other_fields.setdefault('is_active', True)
           #using the general function for creating user, set user
           user = self._create_user(email=email, tel_number=tel_number, username=username, password=password, **other_fields)
           user.is_staff = True
           user.is_superadmin = True
           user.is_admin = True
           user.save(using=self._db)
           return user