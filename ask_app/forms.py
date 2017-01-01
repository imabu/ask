#-*- coding: utf-8-*-
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from ask_app.models import Profile
from django.core.exceptions import ObjectDoesNotExist

class RegistrationForm(UserCreationForm):
	email=forms.EmailField(
		required=True, 
		error_messages={'required':'Введите email'}
		)
	nickname = forms.CharField(required=True, error_messages = {'required':'Введите псевдоним'})
	avatar = forms.ImageField(required=False)
	class Meta:
		model=User
		fields=('username','nickname', 'email','password1', 'password2','avatar')
	def clean(self):
		data=self.cleaned_data
		return data

	def clean_email(self):
		email=self.cleaned_data["email"]
		try:
			User._default_manager.get(email=email)
		except User.DoesNotExist: 
			return email
		raise forms.ValidationError('Такой адрес уже существует')
		return self.cleaned_data

	def clean_nickname(self):
		nickname=self.cleaned_data["nickname"]
		try:
			Profile._default_manager.get(nickname=nickname)
		except Profile.DoesNotExist: 
			return nickname
		raise forms.ValidationError('Такой псевдоним уже существует')
		return self.cleaned_data

	def save(self):
		user=User.objects.create_user(self.cleaned_data['username'],self.cleaned_data['email'], self.cleaned_data['password1'])
		user.save()
		profile=Profile.objects.create(user=user, nickname=self.cleaned_data['nickname'], avatar=self.cleaned_data['avatar'])
		profile.save()
