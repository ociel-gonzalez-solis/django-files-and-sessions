from django import forms

class ProfileForm(forms.Form):
    user_img = forms.ImageField()
