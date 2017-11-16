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
				form.add_error('email', 'Wrong username or password.')
		
		except mdb.Error as e:
		  
			print(e.args[0], e.args[1])

		except:
			
			form.add_error('email', 'Wrong username or password.')

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

		email = form['email'].value()
		password = form['password1'].value()
		name = form['name'].value()
		city = form['city'].value()
		state = form['state'].value()
		phoneNumber = form['phoneNumber'].value()
		birthDate = form['birthDate'].value()

		try:
			con = mdb.connect('localhost', 'root', 'password', 'healthmanagement')
			
			'''
			query = "INSERT into patient values (null,\'"
			query += name
			query += "\',\'"
			query += phoneNumber
			query += "\',\'"
			query += city
			query += "\',\'"
			query += state
			query += "\',\'"
			query += birthDate
			query += "\',\'"
			query += email
			query += "\',\'"
			query += password
			query += "\');"
			'''

			query = "INSERT into patient VALUES(null,'%s','%s','%s','%s','%s','%s','%s')" % (name, phoneNumber, city, state, birthDate, email, password) + ';'

			con.cursor().execute(query)
			con.commit()

		except mdb.Error as e:
		  
			print(e.args[0], e.args[1])

		except:
			print('Database query failed.')

		finally:
		
			if con:
				con.close()

	else:
		form = SignUpForm()
	
	return render(request, 'smcapp/reg_form.htm', {'form': form})









