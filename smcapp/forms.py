from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
	MAX_LENGTH = 20

	email = forms.EmailField(label='Username', max_length=MAX_LENGTH, widget=forms.TextInput(attrs={'style':'width:300;'}))
	password = forms.CharField(label='Password', max_length=MAX_LENGTH, widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'password1', 'password2')
		widgets = {
			'password' : forms.PasswordInput(),
		}

class SignUpForm(UserCreationForm):
	MAX_LENGTH = 20

	email = forms.EmailField(label='Email', max_length=150, required=True, help_text='Required. Enter a valid email address.')
	name = forms.CharField(label='Name', max_length=30, required=False)
	password1 = forms.CharField(label='Password', max_length=MAX_LENGTH, widget=forms.PasswordInput())
	password2 = forms.CharField(label='Verify Password', max_length=MAX_LENGTH, widget=forms.PasswordInput())
	city = forms.CharField(label='City', max_length=10)
	state = forms.CharField(label='State', max_length=10)
	birthDate = forms.CharField(label='Birth Date', max_length=10)
	phoneNumber = forms.CharField(label='Phone Number', max_length=10)

	class Meta:
		model = User
		fields = ('email', 'name', 'password1', 'password2', 'city', 'state', 'birthDate')
		widgets = {
			'password' : forms.PasswordInput(),
		}
