from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from smcapp.forms import SignUpForm
from .forms import LoginForm
import MySQLdb as mdb

def  index(request):
	return render(request, 'smcapp/index.htm')

def login(request):
	# if this is a POST request we need to process the form data
	if request.method == 'POST':

		try:
			con = mdb.connect('localhost', 'root', '123', 'healthmanagement')
				
			con.query("SELECT * from patient")
			result = con.use_result()
		
			print(result.fetch_row()[0])
		
		except:
		  
			print(e.args[0], e.args[1])
			sys.exit(1)

		finally:
		
			if con:
				con.close()

		# create a form instance and populate it with data from the request:
		form = LoginForm(request.POST)

		print(form['email'].value())

		# check whether it's valid:
		if form.is_valid() and form['email'].value() == "joshua@cs.ucf.edu":
			# process the data in form.cleaned_data as required
			# ...
			# redirect to a new URL:
			return HttpResponseRedirect('/admin/')

	# if a GET (or any other method) we'll create a blank form
	else:
		form = LoginForm()

	return render(request, 'smcapp/login.htm', {'form': form})

def register(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		# once the information is check for being "unique" save the information
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return HttpResponseRedirect('/admin/')
	# else create a user form to register
	else:
		form = SignUpForm()
		args = {'form': form}
		return render(request, 'smcapp/reg_form.htm', args)
