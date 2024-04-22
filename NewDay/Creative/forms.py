from django import forms
from . models import Register

class Registerform(forms.ModelForm):
    Password=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)
    Confirmpassword=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)
    class Meta():
        model=Register
        fields='__all__'
class Loginform(forms.ModelForm):
    Password=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)
    class Meta():
        model=Register
        fields=('Email','Password')

class Updateform(forms.ModelForm):
    class Meta():
        model=Register
        fields=('Name','Age','Place','Email')
        
class ChangepasswordForm(forms.ModelForm):
    Oldpassword=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)
    Newpassword=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)
    Confirmpassword=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)
    class Meta():
        model=Register
        fields=('Oldpassword','Newpassword','Confirmpassword')