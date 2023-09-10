from django import forms
from django.contrib.auth.models import User
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