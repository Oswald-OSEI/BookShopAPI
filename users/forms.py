from django import forms
from .models import CustomUser
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password

#Model forms

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(max_length=16, label = 'Password', widget=forms.PasswordInput)
    password_again = forms.CharField(max_length=16, label = 'Repeat Password', widget=forms.PasswordInput)
    
    class Meta:
        model = CustomUser 
        fields = ["first_name", "last_name","middle_name", "username", "email", "tel_number", "status","postal_address", "house_address", "City", "region", "country", "profile_picture"]
        
        labels = {
            'password_again': "Repeat Password", 
            'password': "Password",
            "status": "Gender"
            
            #'start_date': "Date of Registration"
        }
        
        def clean_password_again(self):
            initial = self.cleaned_data['password']
            final =  self.cleaned_data['password_again']
            
            if final != initial:
                raise forms.ValidationError("Password don't match")
        
            return final 

class LoginForm(forms.Form):
    email = forms.EmailField( label = 'Email')
    Password = forms.CharField(label='Password', widget= forms.PasswordInput)