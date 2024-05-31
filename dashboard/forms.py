from typing import Any
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 


class UserForms(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name',]


    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(UserForms, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'

class UserCreate(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']   


    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(UserCreate, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'