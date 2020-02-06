from django import forms

class PictureForm(forms.Form):

    name = forms.CharField(label='name', max_length=100)
    photo = forms.ImageField()
