from django import forms
from django.contrib.auth.forms import UserCreationForm, User, AuthenticationForm, UsernameField, PasswordChangeForm,SetPasswordForm

from .models import *
class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': 'True', 'class': 'form-control'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'form-control'}))


class CustomRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': 'True', 'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# class CustomerRegistrationForm(UserCreationForm):
#     username = forms.CharField(widget=forms.TextField(attrs = {'autofocus': 'True',' class'= 'form-control'}))
#     email = forms.CharField(widget=forms.EmailField(attrs={'class'= 'form-control'}))
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput (attrs={'class'= 'form-control'}))
#     password2 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class' = 'form-control'}))
class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='OLD PASSWORD', widget=forms.PasswordInput(attrs={'autofocus':'True', 'class':'form-control'}))
    new_password1 = forms.CharField(label='New PASSWORD',widget=forms.PasswordInput(attrs={'autofocus': 'True', 'class': 'form-control'}))
    new_password2 = forms.CharField(label='Confirm PASSWORD', widget=forms.PasswordInput(attrs={'autofocus':'True', 'class':'form-control'}))
class MyPasswordResetForm(PasswordChangeForm):
    email= forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
class CustomerProfileForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ['id', 'name', 'locality', 'mobile', 'city', 'state', 'zipcode']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'locality': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'zipcode': forms.NumberInput(attrs={'class': 'form-control'}),

        }

class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label='New PASSWORD',
                                   widget=forms.PasswordInput(attrs={'autofocus': 'True', 'class': 'form-control'}))
    new_password2 = forms.CharField(label=' Confirm New PASSWORD',
                                    widget=forms.PasswordInput(attrs={'autofocus': 'True', 'class': 'form-control'}))


