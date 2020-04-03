from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django import forms
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    email=forms.EmailField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email address'}))
    first_name=forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First name'}))
    last_name=forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last name'}))

    class Meta:
        model=User
        fields=('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['class']='form-control'
        self.fields['username'].label=''
        self.fields['password1'].label=''
        self.fields['password2'].label=''
        self.fields['username'].widget.attrs['placeholder']='Username'
        self.fields['password1'].widget.attrs['placeholder']='Password'
        self.fields['password2'].widget.attrs['placeholder']='Confirm password'


class EditProfileForm(UserChangeForm):
    email=forms.EmailField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email address'}))
    first_name=forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First name'}))
    last_name=forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last name'}))

    class Meta:
        model=User
        fields=('username', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['username'].label=''
        self.fields['username'].widget.attrs['placeholder']='Username'


class ChangePasswordForm(PasswordChangeForm):

    class Meta:
        model=User
        fields=('password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['class']='form-control'
        self.fields['password1'].label=''
        self.fields['password2'].label=''
        self.fields['password1'].widget.attrs['placeholder']='Password'
        self.fields['password2'].widget.attrs['placeholder']='Confirm password'