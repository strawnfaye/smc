from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from smcapp.forms import SignUpForm
from .forms import LoginForm
import MySQLdb as mdb

def index(request):
	return render(request, 'smcapp/index.htm')

def login(request):

	# if this is a POST request we need to process the form data
	if request.method == 'POST':

		# create a form instance and populate it with data from the request:
		form = LoginForm(request.POST)

		try:
			con = mdb.connect('localhost', 'root', 'password', 'healthmanagement')
			
			query = "SELECT userName, userPassWord from patient where userName = \'" + form['email'].value() + "\';"
			con.query(query)
			result = con.use_result()
		
			row = result.fetch_row()[0]

			password = row[1]

			if password != form['password'].value():
				form.add_error('password', 'Wrong password.')
		
		except mdb.Error as e:
		  
			print(e.args[0], e.args[1])

		except:
			
			print("Username does not exist.")

		finally:
		
			if con:
				con.close()

		# check whether it's valid:
		if form.is_valid():
			# process the data in form.cleaned_data as required
			# ...
			# redirect to a new URL:
			return render(request, 'smcapp/login.htm', {'form': form})

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
