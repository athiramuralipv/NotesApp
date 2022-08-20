from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from notes.models import UserProfile,Notes


class UserProfileFrom(ModelForm):
    class Meta:
        modal=UserProfile
        fields=[
            "first_name",
            "last_name",
            "username",
            "email",
        ]
class NotesForm(ModelForm):
    class Meta:
        model = Notes
        fields = [
            "title",
            "notes",
            "image"
        ]

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "notes": forms.Textarea(attrs={"class": "form-control"}),
            "image": forms.FileInput(attrs={"class": "form-control"})
        }

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=[
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2"
            ]
class LoginForm(forms.Form):
    name=forms.CharField(label="Username")
    password=forms.CharField(label="Password")
