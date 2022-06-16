from logging import PlaceHolder
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import *
class UserAdminCreationForm(UserCreationForm):
    """
    A Custom form for creating new users.
    """

    class Meta:
        model = get_user_model()
        fields = ['email','first_name','last_name','phone','dob','address','password1','password2']
        labels={
           'email':'Email',
           'first_name':'First Name',
           'last_name':'Last Name',
           'phone':'Mobile Number',
           'dob':'Date of Birth',
           'address':'Address',
           'password1':'Password1',
           'password2':'Password2',

       

        }

        widgets= {
            'first_name': forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}),
            'last_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}),
            'address': forms.TextInput(attrs={'class':'form-control','placeholder':'Address'}),
            'phone': forms.TextInput(attrs={'class':'form-control','placeholder':'Mobile Number'}),
            'dob': forms.TextInput(attrs={'class':'form-control','placeholder':'Date of birth'}),
            'email': forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
            'password1':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),
            'password2':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),
            
        }