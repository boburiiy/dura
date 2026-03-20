from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=False)
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'profile_img', 'email', 'age', 'bio')

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)