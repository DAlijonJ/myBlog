from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Posts, Comment


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class CreatePost(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ["title", "text", "img"]


class CreateComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["comment"]
