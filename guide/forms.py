from django import forms
from django.contrib.auth.models import User
from . import models

class SignupForm(forms.Form):
    email=forms.CharField(label='Email address',max_length=60,required=True)
    username=forms.CharField(label='Username',max_length=30,required=True,help_text='This will be displayed as your Username')
    password1=forms.CharField(label='Enter Password',max_length=20,required=True,widget=forms.PasswordInput)
    password2=forms.CharField(label='Confirm Password',max_length=20,required=True,widget=forms.PasswordInput)
    phone=forms.IntegerField(label='Phone Number',required=True)
    city=forms.CharField(label='Recidence City')
    class Meta:
        model= User
        fields= ('email','username','password1','password2','phone','city')
    def clean_username(self):
    	user = self.cleaned_data.get('username').lower()
    	check = User.objects.filter(username=user)
    	if check.count() > 0:
    		raise forms.ValidationError(' the username is already taken')
    	else:
    		return user
    def clean_password2(self):
    	password1 = self.cleaned_data.get('password1')
    	password2 = self.cleaned_data.get('password2')
    	if password1 != password2:
    		raise forms.ValidationError('Please enter same passwords both the times')
    	if not(password1) and not(password2):
    		raise forms.ValidationError('Please fill the password fields')
    	if len(password1) < 8:
    		raise forms.ValidationError('The password must be 8 chars ')
    	return True

    def clean_email(self):
        email = self.cleaned_data.get('email')
        check = User.objects.filter(email=email)
        if check.count() > 0:
            raise forms.ValidationError('The email already exists')
        return email

    def save(self):
        user=User.objects.create_user(
        username=self.cleaned_data.get('username'),
        password=self.cleaned_data.get('password1'),
        email=self.cleaned_data.get('email'),
        )
