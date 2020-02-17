from django import forms
from .models import PictureGroup


class PictureForm(forms.Form):

    name = forms.CharField(label='name', max_length=100)
    photo = forms.ImageField()
    description = forms.CharField(label='description', widget=forms.Textarea)
    group_id = forms.CharField(label='description', widget=forms.Select(choices=[("-", "-")]))

class LogInForm(forms.Form):

    user_name = forms.CharField(label='name', max_length=100)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
