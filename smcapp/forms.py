from django import forms

class LoginForm(forms.Form):
	MAX_LENGTH = 20

	email = forms.EmailField(label='Username', max_length=MAX_LENGTH, widget=forms.TextInput(attrs={'style':'width:300;'}))
	password = forms.CharField(label='Password', max_length=MAX_LENGTH)
