from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm

from .models import login_test
#  login form

class UserLoginForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class':"nom" ,'name':"user" ,'placeholder':"your name plz"}))

    email = forms.CharField(widget=forms.TextInput(
        attrs={'class':"email", 'name':"email" ,'type':"email", "placeholder":"your adress email hhh"}))
        
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class':"psd" ,'placeholder': 'Password','placeholder':"Passwordnnn"}))

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

        for fieldname in ["username", "password"]:
            self.fields[fieldname].help_text = None
        
    class Meta:
        model = User
        fields = ("username" ,"email", "password")

class UserRegistreform(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model=User 
        fields=['username','email']


class gamer_login(forms.ModelForm):


    class Meta:
        model = User
        fields = '__all__'

