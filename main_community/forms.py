from django import forms

class Login(forms.Form):
    email = forms.EmailField()
    passwor = forms.CharField(widget=forms.PasswordInput) # passwor because password it's already exist name


class Signup(forms.Form):
    name = forms.CharField(max_length=40)
    email = forms.EmailField()
    passwd = forms.CharField(widget=forms.PasswordInput)
    re_pass= forms.CharField(widget=forms.PasswordInput)
    # pic = forms.ImageField()
