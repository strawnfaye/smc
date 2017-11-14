from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
	MAX_LENGTH = 20

	email = forms.EmailField(label='Username', max_length=MAX_LENGTH, widget=forms.TextInput(attrs={'style':'width:300;'}))
	password = forms.CharField(label='Password', max_length=MAX_LENGTH, widget=forms.PasswordInput(), help_text='Wrong password.')

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'password1', 'password2')
		widgets = {
			'password' : forms.PasswordInput(),
		}

class SignUpForm(UserCreationForm):
	MAX_LENGTH = 20

	username = forms.EmailField(max_length=150, required=True, help_text='Required. Enter a valid email address.')
	first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
	last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
	password1 = forms.CharField(label='Password', max_length=MAX_LENGTH, widget=forms.PasswordInput())
	password2 = forms.CharField(label='Verify Password', max_length=MAX_LENGTH, widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'password1', 'password2')
		widgets = {
			'password' : forms.PasswordInput(),
		}
