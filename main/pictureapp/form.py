from django import forms


class PictureForm(forms.Form):

    name = forms.CharField(label='name', max_length=100)
    photo = forms.ImageField()
    description = forms.CharField(label='description', widget=forms.Textarea)


class LogInForm(forms.Form):

    user_name = forms.CharField(label='name', max_length=100)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
