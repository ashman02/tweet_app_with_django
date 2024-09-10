from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TweetForm(forms.ModelForm):
    
    class Meta:
        model = Tweet
        # for custom forms we use array 
        fields = ['text', 'photo']


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        # for built in forms we use tuples 
        fields = ("username", "email", "password1", "password2")