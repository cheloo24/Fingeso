from django import forms
from models import *
from django.contrib.auth.models import *

from django.forms import Form
from likert_field.forms import LikertFormField

class SurveyForm(Form):
    i_like_snakes = LikertFormField()

class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput())
	password = forms.CharField(widget=forms.PasswordInput(render_value=False))

class RegisterForm(forms.Form):
	username= forms.CharField(label= "Nombre de Usuario", widget=forms.TextInput())
	email = forms.EmailField(widget=forms.TextInput())
	password_one = forms.CharField(label="Password", widget=forms.PasswordInput(render_value=False))
	password_two = forms.CharField(label="Confirmar Password", widget=forms.PasswordInput(render_value=False))

	def clean_username(self):
		username= self.cleaned_data['username']
		try:
			u = User.objects.get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError('Nombre de usuario ya existe')

	def clean_email(self):
		email= self.cleaned_data['email']
		try:
			u = User.objects.get(email=email)
		except User.DoesNotExist:
			return email
		raise forms.ValidationError('Email ya registado')
	
	def clean_password_two(self):
		password_one = self.cleaned_data['password_one']
		password_two = self.cleaned_data['password_two']
		if password_one == password_two:
			pass
		else:
			raise forms.ValidationError('Password no coinciden')


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')

class PerfilForm(forms.ModelForm):
    class Meta:
        model = userProfile
        fields = ('photo', 'direccion')

	
