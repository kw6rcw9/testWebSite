from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Enter Email', required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}))
    username = forms.CharField(label='Enter login', required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter login'}))
    # some = forms.ModelChoiceField(queryset=User.objects.all())
    password1 = forms.CharField(label='Enter password', required=True, 
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm password', required=True, 
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['email', 'username']

class UserUpdateForm(forms.ModelForm):
     email = forms.EmailField(label='Enter Email', required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}))
     username = forms.CharField(label='Enter login', required=True,
         widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter login'}))
     class Meta:
         model = User
         fields = ['username', 'email']

class ProfileImageForm(forms.ModelForm):
    img = forms.ImageField(label='Upload photo', required=False, widget=forms.FileInput)
        
    class Meta:
        model = Profile
        fields = ['img']