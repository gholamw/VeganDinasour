from flask import Flask,request, url_for, redirect, render_template, session
from pypaytabs import Paytabs
from pypaytabs import Utilities as util
#import moyasar
#import braintree
from werkzeug.datastructures import ImmutableOrderedMultiDict
import requests
from flask_mysqldb import MySQL
#from MySQL import escape_string as thwart
#from passlib.hash import sha256_crypt
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask_wtf import FlaskForm
#from wtforms import StringField, PasswordField, BooleanField, SubmitField
#from wtforms.validators import DataRequired
from sqlalchemy import exists
from sqlalchemy import Column, Integer, String
from sqlalchemy import Table, Text
from sqlalchemy import *
from sqlalchemy.schema import DropTable, DropConstraint
import threading
#from flask_login import LoginManager
from flask import jsonify
from flask_mobility import Mobility

from flask import Blueprint

import time
import atexit
import datetime
from datetime import date, timedelta
#from flask_socketio import SocketIO, emit

#from twilio.rest import Client
#from twilio.rest import TwilioRestClient
#from datetime import datetime
import math, random 
from apscheduler.schedulers.background import BackgroundScheduler
from collections import Counter

#from flask_wtf import FlaskForm
#from wtforms import StringField, PasswordField, BooleanField, SubmitField
#from wtforms.validators import DataRequired
#import requests

app = Flask(__name__)  # still relative to module
Mobility(app)
#app.config['MYSQL_HOST'] = 'localhost'
#app.config['MYSQL_USER'] = 'root'
#app.config['MYSQL_PASSWORD'] = 'root'
#app.config['MYSQL_DB'] = 'MyDB'

#mysql = MySQL(app)
app.config['SECRET_KEY'] = 'you-will-never-guess'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
#app.run(threaded=True)
db = SQLAlchemy(app)
db.create_all()

#socketio = SocketIO(app)
#login_manager = LoginManager()
#login_manager.init_app(app)
class Cart:
  def __init__(self, products):
    self.products = products

cartItem = Cart([])
shoppingCart = []
shoppingCart1 = []

class Product:
  def __init__(self, name, price):
    self.name = name
    self.price = price    


class PlanFrequency:
  def __init__(self, date, frequency):
    self.date = date
    self.frequency = frequency 
#db.create_all()
#db.create_all()


assigned_plan = " "
start_date_plan = " "
#ipn_confirmation
sem = threading.Semaphore()
#global ipn_data
aa = None
bb = None
cc = None
p_day = None
def print_date_time():
    print(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))
    d1 = datetime.datetime(int("2018"), int("05"), int("03"))
    d2 = datetime.datetime(int("2018"), int("05"), int("05"))
    end_date = datetime.datetime(int("2000"), int("01"), int("01"))
    today_date = datetime.datetime.today()
    print("date::", d1)
    print(today_date)
    month_days = 30
    week_days = 7
   # plan_date = null
    #db.DropTable(Plan)
    #db.session.commit()
    #test = Column('delivery_option', String)
    #Plan.__table__.append_column(test)
    plans = Plan4.query.all()
    for x in plans:
    	#print("plan delivery option: ", x.delivery_option)
    	plan_date = x.start_date
    	if(x.p_type == "Day"):
    		end_date = plan_date + datetime.timedelta(days=1)
    	elif(x.p_type == "Week"):
    		end_date = plan_date + datetime.timedelta(days=week_days)
    	elif(x.p_type == "Month"):	
    		end_date = plan_date + datetime.timedelta(days=month_days)
    	no_of_days_difference = (end_date - (today_date + datetime.timedelta(days=1))).days
    	if x.is_active == "Active":
    		print("££££££££££££££££££££££££££££££££££££££££££££££")
    		print("Start the daily checks")
    		if no_of_days_difference >= 0:
    			print("inside for/if")
    			print("PLAN START DATE", plan_date)
    			if(x.p_type == "Day"):
    				end_date = plan_date + datetime.timedelta(days=1)
    			elif(x.p_type == "Week"):
    				end_date = plan_date + datetime.timedelta(days=week_days)
    			elif(x.p_type == "Month"):	
    				end_date = plan_date + datetime.timedelta(days=month_days)
    			no_of_days_difference = (end_date - (today_date + datetime.timedelta(days=1))).days
				#end_date = plan_date + datetime.timedelta(days=30)
    			print("PLAN END DATE", end_date)
    			print("DIFFERENCE", no_of_days_difference)
    			x.is_active = "Active"
    			x.expiry_date = end_date
    			db.session.commit()
    		else:	
    			print("outside for/if")
    			print("PLAN DATE", plan_date)
    			if(x.p_type == "Day"):
    				end_date = plan_date + datetime.timedelta(days=1)
    			elif(x.p_type == "Week"):
    				end_date = plan_date + datetime.timedelta(days=week_days)
    			elif(x.p_type == "Month"):	
    				end_date = plan_date + datetime.timedelta(days=month_days)
    			no_of_days_difference = (end_date - today_date).days
				#end_date = plan_date + datetime.timedelta(days=30)
    			print("PLAN END DATE", end_date)
    			print("DIFFERENCE", no_of_days_difference)
    			x.is_active = "Expired"
    			x.expiry_date = end_date
    			customer_object = Customer.query.filter_by(mobile=x.customer_mobile).first()
    			customer_object.number_of_plans = str(int(customer_object.number_of_plans) - 1)
    			db.session.commit()

    		if plan_date <= today_date <= end_date:
    			print("Pass")
    			print("===================================")
    		else:
    			print("Dont Pass")
    			print("===================================")	
			#print("inside for loop")
			#x.is_active = False
			#db.session.commit()

		#print(( plan_date - today_date).days)
    return 0


#scheduler = BackgroundScheduler()
#scheduler.add_job(func=print_date_time, trigger="interval", seconds=2000)
#scheduler.start()

# Shut down the scheduler when exiting the app
#atexit.register(lambda: scheduler.shutdown())
@app.before_first_request
def _run_on_start():
    print ("doing something important with")
    print("bewfore first request")
    db.create_all()
	
    #dates()
    #manipulateDb()
    #manipulateDb2()
    #testDbManipulation()
    #session.permanent = False
    global p_day, p_week, p_month
    price_object = Prices.query.all()

	#p_day= Product("Day", 100)
	#p_week= Product("Week", 200)
	#p_month= Product("Month", 1850)

    price_day= Prices(p_type = "Day", amount = 100)
	#db.session.add(p_day)
    price_week= Prices(p_type = "Week", amount = 200)
	#db.session.add(p_week)
    price_month= Prices(p_type = "Month", amount = 1850)
	#db.session.add(p_month)
	#db.session.commit()
    ##db.session.add(price_day)
    ##db.session.add(price_week)
    ##db.session.add(price_month)
    ##db.session.commit()
    price_object = Prices.query.all()
    print(price_object)




    p_day= Product(price_object[0].p_type, price_object[0].amount)
    p_week= Product(price_object[1].p_type, price_object[1].amount)
    p_month= Product(price_object[2].p_type, price_object[2].amount)
    cartItem = Cart([])
    #db.session.add(p_day)
    session['dayPlan'] = 0
    session['monthPlan'] = 0
    session['weekPlan'] = 0
    session['dayPrice'] = price_object[0].amount
    session['weekPrice'] = price_object[1].amount
    session['monthPrice'] = price_object[2].amount
    session['sumOfCart'] = 0
    session['shippingCost'] = 200
    session['vat'] = 0
    session['checkbox'] = True

@app.before_request
def before_request():
    if request.endpoint == 'shoppingcart':
    	print("going to SHOPPING YAAAY")
    	try:
    		print("inside try")
    		print("trying to cause an error", session.get('dayPlan'))
    		num = session.get('dayPlan')
    		if session.get('dayPlan') == None:
    			price_object = Prices.query.all()
		    	session['dayPlan'] = 0
		    	session['monthPlan'] = 0
		    	session['weekPlan'] = 0
		    	session['dayPrice'] = price_object[0].amount
		    	session['weekPrice'] = price_object[1].amount
		    	session['monthPrice'] = price_object[2].amount
		    	session['sumOfCart'] = 0
		    	session['shippingCost'] = 200
		    	session['vat'] = 0
		    	session['checkbox'] = True
    			print()
    		print()
    	except KeyError:
    		print("inside exception handler")
    		price_object = Prices.query.all()
	    	session['dayPlan'] = 0
	    	session['monthPlan'] = 0
	    	session['weekPlan'] = 0
	    	session['dayPrice'] = price_object[0].amount
	    	session['weekPrice'] = price_object[1].amount
	    	session['monthPrice'] = price_object[2].amount
	    	session['sumOfCart'] = 0
	    	session['shippingCost'] = 200
	    	session['vat'] = 0
	    	session['checkbox'] = True
    		print()	
        #return redirect(url_for('login'))    

	#_day = Product(price_object[0].p_type, price_object[0].amount)
	#p_week = Product(price_object[1].p_type, price_object[1].amount)
	#p_month = Product(price_object[2].p_type, price_object[2].amount)

@app.route("/")
def hello():
	db.create_all()
	print(db)
	print("plan4 rows:")
	#print(Plan4.query.all())
	#global p_day, p_week, p_month
	list_of_products=[]
	session['shop'] = list_of_products	
	
	###user = User(email="admin", name="Mansour Barri",admin=True, password="123")
	###db.session.add(user)
	###db.session.commit()
	print("User admin:")
	print(User.query.all())

	price_object = Prices.query.all()
	session['dayPlan'] = 0
	session['monthPlan'] = 0
	session['weekPlan'] = 0
	session['dayPrice'] = price_object[0].amount
	session['weekPrice'] = price_object[1].amount
	session['monthPrice'] = price_object[2].amount
	session['sumOfCart'] = 0
	session['shippingCost'] = 200
	session['vat'] = 0
	session['checkbox'] = True

	#delete all records
	#db.session.query(User).delete()
	#db.session.commit()
	#db.session.query(Customer).delete()
	#db.session.commit()
	#db.session.query(Plan4).delete()
	#db.session.commit()

	#set up admin user

	#user = User(email="admin", name="Mansour",admin=True, password="123")
	#db.session.add(user)
	#db.session.commit()

	print("Cart has: ", cartItem.products)
	print("Product: ", p_day)
	print("Product: ", p_day.name)
	print("Product: ", p_day.price)

	session['logged_in'] = False
	if session['logged_in'] == False:
		session['logged_in'] = False
	return redirect('/pricing.html')	
	#return render_template('home-page.html')	

@app.route('/pricing.html', methods=['GET', 'POST'])
def pricing():
	price_objects = Prices.query.all()
	return render_template('pricing.html', price_objects=price_objects)

@app.route('/menu.html', methods=['GET', 'POST'])
def menu():
	return render_template('menu.html')

@app.route('/addtocart', methods=['GET', 'POST'])
def addtocart():
	return render_template('addtocart.html')			


@app.route('/clearDB', methods=['GET' , 'POST'])
def clearDB():
	db.drop_all()
	db.session.commit()
	plans = Plan4.query.all()
	print("plans:")
	print(plans)
	return "DB is cleared"
	
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/updatecart', methods=['GET', 'POST'])
def updatecart():
	global shoppingCart
	day_plans = session.get('dayPlan')
	print("Cart has: ", day_plans)
	#cartItem.products.append(p_day)
	#cartList = session['shop']
	print("after")
	day_plans = day_plans + 1

	session['dayPlan'] = day_plans
	print("session has: ", session.get('dayPlan'))
	#session["cart"] = cartList
	#print("Product: ", p_day)
	#print("Cart has: ", shoppingCart)
	#print(values)
	#flash('You were successfully logged in')
	return "nothing"

@app.route('/removeFromCart', methods=['GET', 'POST'])
def removeFromCart():
	global shoppingCart
	day_plans = session.get('dayPlan')
	print("Cart has: ", day_plans)
	#cartItem.products.append(p_day)
	#cartList = session['shop']
	print("after")
	if day_plans > 0:
		day_plans = day_plans - 1

	session['dayPlan'] = day_plans
	print("session has: ", session.get('dayPlan'))
	#session["cart"] = cartList
	#print("Product: ", p_day)
	#print("Cart has: ", shoppingCart)
	#print(values)
	#temp = shoppingcart()
	#print("temp: ", temp)
	#return temp
	return redirect('/shoppingcart')		

@app.route('/updatecart11', methods=['GET', 'POST'])
def updatecar11():
	global shoppingCart
	day_plans = session.get('dayPlan')
	print("Cart has: ", day_plans)
	#cartItem.products.append(p_day)
	#cartList = session['shop']
	print("after")
	day_plans = day_plans + 1

	session['dayPlan'] = day_plans
	print("session has: ", session.get('dayPlan'))
	#session["cart"] = cartList
	#print("Product: ", p_day)
	#print("Cart has: ", shoppingCart)
	#print(values)
	#temp = shoppingcart()
	#print("temp: ", temp)
	return redirect('/shoppingcart')	   

@app.route('/updatecart2', methods=['GET', 'POST'])
def updatecart2():
	global shoppingCart
	month_plans = session.get('monthPlan')
	print("Cart has: ", month_plans)
	print("after")
	month_plans = month_plans + 1
	session['monthPlan'] = month_plans
	print("session has: ", session.get('monthPlan'))
	return "nothing"

@app.route('/removeFromCart2', methods=['GET', 'POST'])
def removeFromCart2():
	global shoppingCart
	month_plans = session.get('monthPlan')
	print("Cart has: ", month_plans)
	print("after")
	if month_plans > 0:
		month_plans = month_plans - 1
	session['monthPlan'] = month_plans
	print("session has: ", session.get('monthPlan'))
	#temp = shoppingcart()
	#print("temp: ", temp)
	#return temp
	return redirect('/shoppingcart')		

@app.route('/updatecart22', methods=['GET', 'POST'])
def updatecart22():
	global shoppingCart
	month_plans = session.get('monthPlan')
	print("Cart has: ", month_plans)
	print("after")
	month_plans = month_plans + 1
	session['monthPlan'] = month_plans
	print("session has: ", session.get('monthPlan'))
	#temp = shoppingcart()
	#print("temp: ", temp)
	#return temp
	return redirect('/shoppingcart') 	   


@app.route('/updatecart3', methods=['GET', 'POST'])
def updatecart3():
	global shoppingCart
	week_plans = session.get('weekPlan')
	print("Cart has: ", week_plans)
	print("after")
	week_plans = week_plans + 1
	session['weekPlan'] = week_plans
	print("session week has: ", session.get('weekPlan'))
	#print(values)
	return "nothing"

@app.route('/removeFromCart3', methods=['GET', 'POST'])
def removeFromCart3():
	global shoppingCart
	week_plans = session.get('weekPlan')
	print("Cart has: ", week_plans)
	print("after")
	if week_plans > 0:
		week_plans = week_plans - 1
	session['weekPlan'] = week_plans
	print("session week has: ", session.get('weekPlan'))
	#print(values)
	#temp = shoppingcart()
	#print("temp: ", temp)
	#return temp
	return redirect('/shoppingcart')		

@app.route('/updatecart33', methods=['GET', 'POST'])
def updatecart33():
	global shoppingCart
	week_plans = session.get('weekPlan')
	print("Cart has: ", week_plans)
	print("after")
	week_plans = week_plans + 1
	session['weekPlan'] = week_plans
	print("session week has: ", session.get('weekPlan'))
	#print(values)
	#temp = shoppingcart()
	#print("temp: ", temp)
	#return temp	   
	return redirect('/shoppingcart')

@app.route('/addDelivery', methods=['GET', 'POST'])
def addDelivery():
	cost = session.get('shippingCost')
	cost = cost + 200
	session['shippingCost'] = cost
	session['checkbox'] = True
	print("is checkbox checked ?", session.get('shippingCost'))
	print("check box val on add is " , session.get('checkbox'))

	#print("session week has: ", session.get('weekPlan'))
	#print(values)
	#temp = shoppingcart()
	#print("temp: ", temp)
	#return temp	   
	return redirect('/shoppingcart')

@app.route('/deleteDelivery', methods=['GET', 'POST'])
def deleteDelivery():
	cost = session.get('shippingCost')
	cost = 0
	session['shippingCost'] = cost
	print("is checkbox checked ? " , request.form["param"])
	session['checkbox'] = False
	#print(values)
	#temp = shoppingcart()
	#print("temp: ", temp)
	#return temp	   
	return redirect('/shoppingcart')		

###############Sign up methods################################
@app.route("/signupDay",methods=['GET', 'POST'])
def signupDay():
	block_dates = testDbManipulation()
	block_dates_confimed = []
	for k,v in block_dates.items():
		if v > 100:
			block_dates_confimed.append(str(k))
			print(k)
	print("Blocked dates are: ", block_dates_confimed)		
	return render_template('mobile-check.html', plan="Day", planPrice=130, blocked_dates=block_dates_confimed)	  


@app.route("/pick-start-date",methods=['GET', 'POST'])
def pickStartDate():
	block_dates = testDbManipulation()
	block_dates_confimed = []
	for k,v in block_dates.items():
		if v > 100:
			block_dates_confimed.append(str(k))
			print(k)
	print("Blocked dates are: ", block_dates_confimed)		
	return render_template('pick-start-date.html', plan="Day", planPrice=130, blocked_dates=block_dates_confimed)	  


@app.route("/signupMonth",methods=['GET', 'POST'])
def signupMonth():
	return render_template('signup-page.html', plan="Month", planPrice=2100)	  

@app.route("/signupWeek",methods=['GET', 'POST'])
def signupWeek():
	return render_template('signup-page.html', plan="Week", planPrice=599)	  

@app.route("/signupLunchWeek",methods=['GET', 'POST'])
def signupLunchWeek():
	return render_template('signup-page.html')	  

@app.route("/signupLunchMonth",methods=['GET', 'POST'])
def signupLunchMonth():
	return render_template('signup-page.html')

@app.route("/smartpmnt",methods=['GET', 'POST'])
def smartpmnt():
	return render_template('smart_payment.html')

@app.route("/shake",methods=['GET', 'POST'])
def shake():
	return render_template('shake.html')

@app.route("/paytabs",methods=['GET', 'POST'])
def paytabs():
	return render_template('paytabs.html')		

@app.route("/terms-and-conditions",methods=['GET', 'POST'])
def termsAndConditions():
	return render_template('terms_and_conditions.html')	

@app.route("/contact-us",methods=['GET', 'POST'])
def contactUS():
	return render_template('contact-us.html')		

#@socketio.on('disconnect')
#def disconnect_user():
#    print("user closes window")	

@app.route("/shoppingcart",methods=['GET', 'POST'])
def shoppingcart():
	print("The checkbox status is: ", session.get('checkbox'))
	status_of_checkbox = session.get('checkbox')
	print("Shippign cost is: ", session.get('shippingCost'))
	global shoppingCart
	print("Cart has the following: ", cartItem.products)
	sum_of_products = 0
	cart = session.get('shop')
	day_plans = session.get('dayPlan')
	day_prices = session.get('dayPrice')
	day_prices = day_prices * day_plans
	day = (day_plans, "Day", day_prices)
	print("tuple day:", day)
	print("tuple day option 1: ", day[0])
	print("tuple day option 2: ", day[1])
	print("tuple day option 3: ", day[2])
	print("Sum: ", day_prices)
	day_list = [day_plans, "Day", day_prices]

	month_plans = session.get('monthPlan')
	month_prices = session.get('monthPrice')
	#week_prices = session.get('weekPrice')
	print("month plans #: ", month_plans)
	print("month prices : ", month_prices)
	#print("week prices : ", week_prices)
	month_prices = month_prices * month_plans
	month = (month_plans, "Month", month_prices)

	week_plans = session.get('weekPlan')
	week_prices = session.get('weekPrice')
	print("week plans #: ", week_plans)
	print("week prices : ", week_prices)
	week_prices = week_prices * week_plans
	week = (week_plans, "Week", week_prices)

	if month_plans >= 1 and status_of_checkbox == True:
		print("month shipping")
		session['shippingCost'] = 200
	elif month_plans <= 0 and week_plans >= 1 and status_of_checkbox == True:
		print("week shipping")
		session['shippingCost'] = 100
	elif month_plans <= 0 and week_plans <= 0 and day_plans >=1 and status_of_checkbox == True:
		print("day shipping")
		session['shippingCost'] = 20
	elif month_plans == 0 and week_plans == 0 and day_plans == 0 and status_of_checkbox == True:
		session['shippingCost'] = 0			
	else:		
		print("no shipping cost chanaged")	
	sum_cart = session.get('sumOfCart')
	shipping_cost = session.get('shippingCost')
	vat = session.get('vat')

	if status_of_checkbox == False:
		print("Turn off")
		session['shippingCost'] = 0

	#for x in cart:
		#sum_of_products = sum_of_products + x.price

	#print("sum of products are: ", sum_of_products)
	sum_of_products = week_prices + month_prices + day_prices + shipping_cost
	vat = sum_of_products * 0.15
	#sum_of_products = sum_of_products + vat
	sum_of_products = sum_of_products
	session['vat'] = vat
	session['sumOfCart'] = sum_of_products
	session["customer_delivery"] = status_of_checkbox
	checkbox = session.get('checkbox')
	return render_template('shopping-cart.html', products=day, products_month=month, products_week=week, sum=sum_of_products,
		shipping_cost=shipping_cost, vat=vat, chk_box=checkbox)		

@app.route("/completeSignup",methods=['GET', 'POST'])
def completeSignup():
	print("inside /completeSignup")
	email_part1 = " "
	d_option = " "
	shipping_amount=" "
	if request.method == 'POST':
		print("yes post method")
		print(request.form)  
		#email = request.form["email"]  
		fname = request.form["fname"]
		startDate = request.form["datepicker"]  
		plan = request.form["plan"]  
		#password = request.form["pswd"]
		session['customer_start_date'] = startDate
		#delivery = request.form["delivery"]
		delivery = "NOD"
		mobile = request.form["mobile"]
		print("Mobile: ", mobile)
		print("DELIVERY :", delivery)
		if "Yes" in delivery:
			d_option = "D"
		else:
			d_option = "NOD"	
		  

		#print(request.args.get('form_name') )	
		#email = request.form.get("email")
		#email = request.args.get('email')
		#print(email)
		print(fname)
		print(plan)
		print("START DATE",startDate)
		#print(password)
		start_date_plan = startDate
		assigned_plan = plan

		print(start_date_plan)
		print("checkpoint")
		users = User.query.all()

		print("Users", users)
		user_email = User.query.filter_by(email = email).first()
		#ret = query(exists().where(users.email==email)).scalar()
		#print("does it exist ? ", ret)
		print("check .. ",User.query.filter_by(email = email))
		if User.query.filter_by(email = email).first() != None:
			print("User Exists")
		else:
			print('User doesn\'t exist.')
			db.session.add(user)
			db.session.commit()
			session["user"] = user.email
			session['this_one'] = '1'
			#pId = session['email']
			#print("current user: ",pId)
			#it = session.get('email')
			#print("current user check", it)
			#session.modified = True
			print("user", user)

		users2 = User.query.all()
		print("Users", users2)
		email_part1 = email + "#" + startDate + "#" + d_option
		print("Email - start Date: ", email)
		my_str = email_part1.split('#')
		email_part = my_str[0]
		date_part = my_str[1]
		print("EMAIL PART", email_part)
		print("DATE PART", date_part)
		delivery_part = my_str[2]
		my_str2 = date_part.split('-')
		#print("YEAR: ", my_str2[0])
		#print("MONTH: ", my_str2[1])
		#print("DAY: ", my_str2[2])

		print("D option: ", d_option)
		delivery_option_selected = " "
		if "D" in delivery_part:
			delivery_option_selected = True
			shipping_amount = "0.11"
		if "NOD" in delivery_part:
			delivery_option_selected = False
			shipping_amount = "0.00"
		print("delivery_option_selected:  ", delivery_option_selected)	


		#cur = mysql.connection.cursor()
        #cur.execute("INSERT INTO MyUsers(firstName, lastName) VALUES (%s, %s)", (firstName, lastName))
        #mysql.connection.commit()
        #cur.close()
	else:
		print("no get method")	

	#return render_template('signup-page.html')
	#makePayment();
	print("email_part1 var: ", email_part1)
	print("Shipping amount: ", shipping_amount)
	price_object_required = Prices.query.filter_by(p_type=plan).first()
	price_object_required_amount = price_object_required.amount + float(shipping_amount)
	if "month" in plan:
		return render_template('paypalMonth.html', email=email_part1, startDate=startDate, delivery_option_selected = delivery_option_selected)

	
	session["current_signup_customer"] = mobile
	session["current_signup_customer_name"] = fname
	session["customer_name"] = fname
	session["customer_address"] = "Jeddah"
	session["customer_start_date"] = startDate

	global aa,bb,cc
	aa ,bb, cc = email_part1 , price_object_required_amount, plan
	otp_code = generateOTP()
	session["otp"] = otp_code
	sms_message= "Dear Customer, Welcome to The Vegan Dinasour. The OTP for your transaction is " + otp_code
	print("SMS: ", sms_message)	
	#account_sid = 'AC9d2131f7296e8467f91dc3eccb36fbbb'
	#auth_token = '6f55716b6fcfaa950f1d4c01e5975813'
	#client = Client(account_sid, auth_token)
	#client.messages.create(from_='2062899465',
    #                   to=mobile,
    #                   body=sms_message)
	mob = str(mobile)
	ottp = str(otp_code)
	otp_msg1 = "http://api.smsala.com/api/SendSMS?api_id=API475422013615&api_password=6201620Wg&sms_type=P&encoding=T&sender_id=Vegan%20Dino&phonenumber="+mob
	otp_msg2 = "&textmessage=Your%20OTP%20is%"
	otp_mi="&textmessage=Your OTP is " + ottp
	final_link = otp_msg1 + otp_mi
	otp_req_link = "http://api.smsala.com/api/SendSMS?api_id=API475422013615&api_password=6201620Wg&sms_type=P&encoding=T&sender_id=Vegan%20Dino&phonenumber=" + mob + "&textmessage=Your%20OTP%20is%"+ ottp
	http_req_opt = "http://api.smsala.com/api/SendSMS?api_id=API475422013615&api_password=6201620Wg&sms_type=P&encoding=T&sender_id=Vegan%20Dino&phonenumber=" + mob + "&textmessage=Your%20OTP%20is%" + ottp
	print(otp_mi)
	print(final_link)
	r = requests.get(final_link)				   	
	account_sid = ''
	auth_token = ''
	client = Client(account_sid, auth_token)
	client.messages.create(from_='2062899465',
                       to=mobile,
                       body=sms_message)	
	return render_template('otp.html', email_part1 = aa, price_object_required_amount = bb ,  plan = plan)
	#return render_template('paypal.html', email=email_part1, startDate=startDate, delivery_option_selected=delivery_option_selected, shipping_amount=shipping_amount, 
	#	amount = price_object_required_amount, plan = plan)
	#return "Welcome to payment page"
	
##############################################################
@app.route("/otp-check",methods=['GET', 'POST'])
def otpCheck():
	mobile2 = request.form["mobile"]
	#mobile = session.get('customer_login_mobile')
	session['customer_login_mobile'] = mobile2
	otp_code = generateOTP()
	session["otp"] = otp_code
	sendOTP(mobile2, otp_code)
	return render_template('otp-check.html')

@app.route("/complete-customer-signup",methods=['GET', 'POST'])
def signUpFirstTimeCustomer():
	fname = request.form["fname"]
	startDate = request.form["datepicker"]  
	plan = request.form["plan"]  
	#password = request.form["pswd"]
	session['customer_start_date'] = startDate
	#delivery = request.form["delivery"]
	#mobile = request.form["mobile"]
	#session["current_signup_customer"] = mobile
	session["current_signup_customer_name"] = fname
	session["customer_name"] = fname
	session["customer_address"] = "Jeddah"
	session["customer_start_date"] = startDate
	mobile = session.get('customer_login_mobile')
	start_date = session.get('customer_start_date')
	status_of_checkbox = session.get('checkbox')
	day_plans = session.get('dayPlan')
	week_plans = session.get('weekPlan')
	month_plans = session.get('monthPlan')
	customer_mobile = session.get('current_signup_customer')
	customer_delivery = session.get('customer_delivery')
	customer_name = session.get('customer_name')
	customer_address = session.get('customer_address')
	customer_str_date = session.get('customer_start_date')
	toatl_number_of_plans = day_plans + week_plans + month_plans
	toatl_number_of_plans = str(toatl_number_of_plans)
	print("toatl_number_of_plans ", toatl_number_of_plans)
	customer = Customer(mobile=mobile, name=customer_name,number_of_plans = toatl_number_of_plans,
	number_of_bags = toatl_number_of_plans , special_customer = "No",address = customer_address, 
	delivery_option = status_of_checkbox)
	db.session.add(customer)
	db.session.commit()
	date_array = start_date.split("/")
	day = date_array[1]
	day_int = int(day)
	month = date_array[0]
	month_int = int(month)
	year = date_array[2]
	year_int = int(year)

	date = datetime.datetime(year_int, month_int, day_int, 0, 0)
	#date_time_obj = datetime.datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S.%f')
	print('Type of start date!')
	#print(type(date_time_obj))
	print(start_date)
	print(date)
	#for loop for Day 
	customer_name = session.get('current_signup_customer_name')
	for i in range(day_plans):
		plan = Plan4(customer_mobile=customer_mobile, customer_name = customer_name,  start_date=date, p_type = "Day", is_active = "Active", expiry_date= date, number_of_pauses = 0, customer = customer)
		db.session.add(plan)

	#for loop for Week 
	for i in range(week_plans):
		plan = Plan4(customer_mobile=customer_mobile, customer_name = customer_name, start_date=date, p_type = "Week", is_active = "Active", expiry_date= date, number_of_pauses = 0, customer = customer)
		db.session.add(plan)

	#for loop for Month 
	for i in range(month_plans):
		plan = Plan4(customer_mobile=customer_mobile, customer_name = customer_name, start_date=date, p_type = "Month", is_active = "Active", expiry_date= date, number_of_pauses = 0, customer = customer)
		db.session.add(plan)	
	db.session.commit()
	return redirect('/paytabs')
	#return "Complete Customer Registeration"

def addPlansToRegisteredCustomers(mobile):
	customer = Customer.query.filter_by(mobile=mobile).first()

	start_date = session.get('customer_start_date')
	status_of_checkbox = session.get('checkbox')
	day_plans = session.get('dayPlan')
	week_plans = session.get('weekPlan')
	month_plans = session.get('monthPlan')
	customer_mobile = mobile
	customer_name = customer.name
	customer_delivery = session.get('customer_delivery')
	customer_str_date = session.get('customer_start_date')
	toatl_number_of_plans = day_plans + week_plans + month_plans
	toatl_number_of_plans = str(toatl_number_of_plans)
	print("toatl_number_of_plans ", toatl_number_of_plans)

	customer.number_of_plans = str(int(customer.number_of_plans) +  int(toatl_number_of_plans))
	customer.number_of_bags = str(int(customer.number_of_plans) +  int(toatl_number_of_plans))
	print("total number of plans: ")
	print(customer.number_of_plans)
	print("total number of bags: ")
	print(customer.number_of_bags)
	db.session.commit()

	#^^^^
	date_array = start_date.split("/")
	day = date_array[1]
	day_int = int(day)
	month = date_array[0]
	month_int = int(month)
	year = date_array[2]
	year_int = int(year)

	date = datetime.datetime(year_int, month_int, day_int, 0, 0)
	#date_time_obj = datetime.datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S.%f')
	print('Type of start date!')
	#print(type(date_time_obj))
	print(start_date)
	print(date)
	#for loop for Day 
	#customer_name = session.get('current_signup_customer_name')
	for i in range(day_plans):
		plan = Plan4(customer_mobile=customer_mobile, customer_name = customer_name,  start_date=date, p_type = "Day", is_active = "Active", expiry_date= date, number_of_pauses = 0, customer = customer)
		db.session.add(plan)

	#for loop for Week 
	for i in range(week_plans):
		plan = Plan4(customer_mobile=customer_mobile, customer_name = customer_name, start_date=date, p_type = "Week", is_active = "Active", expiry_date= date, number_of_pauses = 0, customer = customer)
		db.session.add(plan)

	#for loop for Month 
	for i in range(month_plans):
		plan = Plan4(customer_mobile=customer_mobile, customer_name = customer_name, start_date=date, p_type = "Month", is_active = "Active", expiry_date= date, number_of_pauses = 0, customer = customer)
		db.session.add(plan)	
	db.session.commit()
	return True

@app.route("/add-plan-completion",methods=['GET', 'POST'])
def addPlanCompletion(): 
	startDate = request.form["datepicker"]  
	session['customer_start_date'] = startDate
	mobile = session.get('customer_login_mobile')
	print("Checking exisiting customer ----> ", mobile)
	res = addPlansToRegisteredCustomers(mobile)
	#return "plans are added!!"
	return redirect('/paytabs')

@app.route("/otp-auth",methods=['GET', 'POST'])
def otpAuth():
	#print(aa)
	#print(bb)
	#print(cc)
	#print(request.form)  
	mobile = session.get('customer_login_mobile')
	print("mobile is ")
	print(mobile)
	#mobile2 = request.form["mobile"]
	#print(mobile2)
	exists = db.session.query(db.exists().where(Customer.mobile == mobile)).scalar()
	if exists == False:
		block_dates = testDbManipulation()
		block_dates_confimed = []
		for k,v in block_dates.items():
			if v > 100:
				block_dates_confimed.append(str(k))
				print(k)
		print("Blocked dates are: ", block_dates_confimed)		
		return render_template('signup-page.html', plan="Day", planPrice=130, blocked_dates=block_dates_confimed)
	print("The Mobile exisit or not ? ")
	print(exists)
	#return "ok!!"
	otp = request.form["OTP"]
	otp_gen = session["otp"]

	print("generated otp: ", session["otp"])
	print(type(otp_gen))
	#print("customer entr otp: ", request.form["otp"])
	#print(type(otp))
	#print(session["otp"] == int(otp))
	if session["otp"] == otp:
		print("OTP matches")
		return redirect('/pick-start-date')
		#return "Two way authentication approved"
	return "Two way authentication denied"	


################## Handling Payments##########################



@app.route('/ipn/',methods=['GET', 'POST'])
def ipn():
	#sem.acquire()
	#print("inside IPN function")
	#try:
		#print("inside TRY statement")	
	arg = ''
	request.parameter_storage_class = ImmutableOrderedMultiDict
	values = request.form
	print("values", values)
	for x, y in values.items():
	 		arg += "&{x}={y}".format(x=x,y=y)

	print("start Authorizing 1")		

	validate_url = 'https://www.paypal.com' \
		'/cgi-bin/webscr?cmd=_notify-validate{arg}' \
		.format(arg=arg)

	print("start Authorizing 2")			   
	r = requests.get(validate_url)
	print("r value", r)
	print("r text", r.text)
	if r.text == 'VERIFIED':
		print("verified")
		#print(session['email'])
		if "user" in session:
			print("user in session")
			user = session["user"]
			print("user is: " , user)
		else:
			print("user not in session")
			#user = session["user"]
			#print("user is: " , user)	
		#it = session.get('user')
		#print("session", it)
		#print("date", start_date_plan)
		#ll = session['email']
	else:
		print("not verified")		 		
		#values = request.form
		#ipn_values = request.form
		#global ipn_data = values
		#processIPN(values)
		#sucess(values)
		#print(values["payment_status"])
		#print("values:", values)
		#print("Payment status", request.form["payment_status"])
		#print("Payment amount", request.form["payment_gross"])

	#pId = session['email']
	#print("SESSION")
	#print("session: ", session['user'])
	user_email = request.form["custom"]
	print("WATCH 1", user_email)
	email_date_parts = user_email.split('#')
	print("WATCH 2", email_date_parts)

	user_email_part = email_date_parts[0]
	print("WATCH 3", user_email_part)

	date_part = email_date_parts[1]
	print("WATCH 4", date_part)

	date_components = date_part.split('-')
	print("WATCH 5", date_components)

	delivery_part = email_date_parts[2]
	print("DEL::", delivery_part)

	year = date_components[0]
	month = date_components[1]
	day = date_components[2]
	start_date_object = datetime.datetime(int(year), int(month), int(day))
	print("look at date: ", start_date_object)
	#delivery = request.form["custom2"]
	#str_date = request.form["invoice"]
	user = User.query.filter_by(email=user_email_part).first()
	print("USER", user)
	print("USER EMAIL", user.email)
	#print("STRT DATE:", str_date)
	#print("D OPTION", custom2)


	payments = Payment.query.all()
	print("Payments before commit", payments)

	#if payments==[]:
		#render_template("success.html")
	#else:
	#	render_template("success.html")	

	payment_id = request.form["txn_id"]
	payment_date=request.form["payment_date"]
	payment_amount=float(request.form["payment_gross"])
	payment_amount = payment_amount * 3.75
	payment_status=request.form["payment_status"]
	payer_paypal_email="gholamw@tcd.ie"
	payer_start_date=date_part
	payer_plan=request.form["item_name"]
	payer_email=user.email


	payment = Payment(payment_id=payment_id, payment_date=payment_date,payment_amount=payment_amount,
		payment_status=payment_status,payer_paypal_email=payer_paypal_email,
		payer_start_date=payer_start_date, payer_plan=payer_plan,payer_email = payer_email)

	payments = Payment.query.all()
	print("Payments before commit", payments)
	db.create_all()

	plans = Plan2.query.all()
	print("plans before commit", plans)

	delivery_option_selected = " "
	if "D" in delivery_part:
		delivery_option_selected = "Yes"
	else:
		delivery_option_selected = "No"	

	plan = Plan2(email=payer_email, payment_id = payment_id, start_date = start_date_object, p_type=payer_plan, is_active = True, 
		delivery_option = delivery_option_selected)
	
	#class Plan(db.Model):
	#id = db.Column(db.Integer, primary_key=True) 
	#email = db.Column(db.String(50), db.ForeignKey('user.email'), primary_key=True)
	#payment_id = db.Column(db.String(50), db.ForeignKey('payment.payment_id'))
	#start_date = db.Column(db.DateTime)
	#p_type = db.Column(db.String(50))
	#is_active = db.Column(db.Boolean, default=False)
	#payment = db.relationship("Payment", back_populates="plan")                            	
	#user = db.relationship("User", back_populates="plan") 


	db.session.add(payment)
	db.session.add(plan)
	db.session.commit()

	payments = Payment.query.all()
	print("Payments after commit", payments)

	plans = Plan2.query.all()
	print("plans after commit", plans)

	return "done"
	# 	sem.release()

	# 	for x, y in values.iteritems():
	# 		print("inside for loop")
	# 		arg += "&{x}={y}".format(x=x,y=y)

		
	# 	print("start Authorizing 1")			   	
	# 	validate_url = 'https://www.sandbox.paypal.com' \
	# 				   '/cgi-bin/webscr?cmd=_notify-validate{arg}' \
	# 				   .format(arg=arg)
	# 	print("validate url:", validate_url)					   
	# 	print("start Authorizing 2")			   
	# 	r = requests.get(validate_url)
	# 	print("r value", r)
	# 	print("r text", r.text)
	# 	tt = getPaymentData();
	# 	if r.text == 'VERIFIED':
	# 		print("verified")
	# 		try:
	# 			payer_email =  thwart(request.form.get('payer_email'))
	# 			unix = int(time.time())
	# 			payment_date = thwart(request.form.get('payment_date'))
	# 			username = thwart(request.form.get('custom'))
	# 			last_name = thwart(request.form.get('last_name'))
	# 			payment_gross = thwart(request.form.get('payment_gross'))
	# 			payment_fee = thwart(request.form.get('payment_fee'))
	# 			payment_net = float(payment_gross) - float(payment_fee)
	# 			payment_status = thwart(request.form.get('payment_status'))
	# 			txn_id = thwart(request.form.get('txn_id'))
	# 		except Exception as e:
	# 			with open('/tmp/ipnout.txt','a') as f:
	# 				data = 'ERROR WITH IPN DATA\n'+str(values)+'\n'
	# 				f.write(data)
			
	# 		with open('/tmp/ipnout.txt','a') as f:
	# 			data = 'SUCCESS\n'+str(values)+'\n'
	# 			f.write(data)

	# 		#c,conn = connection()
	# 		#c.execute("INSERT INTO ipn (unix, payment_date, username, last_name, payment_gross, payment_fee, payment_net, payment_status, txn_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
	# 		#			(unix, payment_date, username, last_name, payment_gross, payment_fee, payment_net, payment_status, txn_id))
	# 		#conn.commit()
	# 		#c.close()
	# 		#conn.close()
	# 		#gc.collect()

	# 	else:
	# 		with open('/tmp/ipnout.txt','a') as f:
	# 			data = 'FAILURE\n'+str(values)+'\n'
	# 			f.write(data)
				
	# 	return r.text
	# except Exception as e:
	# 	return str(e)



@app.route('/success/', methods=['GET', 'POST'])
def success():
	#print("ipn data", ipn_data)
	payments = Payment.query.all()
	print("Payments at sucess", payments)
	print("check inside the payment",payments[1])
	return render_template("success.html")

def processIPN(values):
	print(values)
	return 0;	
def getPaymentData():
	print("Pmnt done")
	return 0

# function to generate OTP 
def generateOTP() : 
  
    # Declare a digits variable   
    # which stores all digits  
    digits = "0123456789"
    OTP = "" 
  
   # length of password can be chaged 
   # by changing value in range 
    for i in range(4) : 
        OTP += digits[math.floor(random.random() * 10)] 
  
    return OTP 	


#################### Payment Functions########################

#@app.route('/complete/<string:name>')
#def completePaypalPayment(name):
#	print("inside functttttopn")
#	print(name)
#	return name; 

### important func###
#@app.route("/<path:path>")
#def index1(path):
#	print("inside babe")
##	#print(path)
#	urll = "" + request.url.rstrip("?")
#	me = "?wessam"
#	me = me.lstrip('?')
#	print(me)
#	print(request.url)
#	if "st=Completedd" in request.url:
#		return "Payment successful"
#	return "payment denied"

#@app.route("/complete/<path:input_url>")
#def index1(input_url):
#	print("it comes here")
#	print(request.query_string)
#	print(input_url)
#	str1 = "?"
#	str2 = input_url
#	newstr = "".join((str1, str2))
#	print(newstr)
#	return newstr

@app.route('/f')
def index66():
	return '<h1> Added New User!</h1>'	


@app.route('/completePayment')
def index12():
	return 'Payment done'		

def paypalPayment():
	return 0;


def makePayment():

	moyasar.api_key = 'sk_test_3BUT3GyCbBhZYgArtmFCG8TWqiLsb9zY31pUtoEG'
	#fetch_invoice = moyasar.Invoice.fetch('<invoice id>')
	#print(fetch_invoice)
	return 0;




def payment():

	secret_key = "n9qAfTSeLpkQZWkF1p7hUwh0MRh5Ily5uZGJTzYEZivYePDffLxahOa4Fr9oMIuhIa0BKYgJhLIvBmLR7i1o7ctNEDbqmFI4QIFB"
	paytab = Paytabs("gholamw@tcd.ie", secret_key) # return an object of paytabs
	ip_c = request.environ['REMOTE_ADDR']
	print(ip_c)
	print(json_dict)
	#authenticate with returned object
	result = paytab.authenticate() # returns PaytabsApiResponse object with response_status and status or exception error (PaytabsApiError: Invalid)
	print('Result', result.data) #Result {'result': 'valid', 'response_code': '4000'} or pypaytabs.Exceptions.PaytabsApiError: invalid



		#Prepare product names list to be passed to create_pay_page method
	products = {'names':['product_1','product_2','product_3'],'quantities':['5','2.5','10'],'prices':['5','8','9']}
	invoice_products = util.prepare_invoice(products)
	#print('Invoice Details: ', invoice_products)  #{'names': 'product_1 || product_2 || product_3', 'prices': '5 || 8 || 9', 'quantities': '5 || 2.5 || 10'}

	#to create pay page, you have to prepare data as dictionary as like:
	pay_data = {"merchant_email":paytab.email, 'secret_key':paytab.key,
	            "site_url" : "http://127.0.0.1:5000",
	            "return_url" : "http://127.0.0.1:5000",
	            "title": "JohnDoe And Co.",
	            "cc_first_name": "John",
	            "cc_last_name": "Doe",
	            "cc_phone_number": "00973",
	            "phone_number": "123123123456",
	            "email": "johndoe@example.com",
	            "products_per_title": invoice_products['names'], #by using invoice_products dictionary returned from prepare_invoice method,
	            "unit_price": invoice_products['prices'],
	            "quantity": invoice_products['quantities'],
	            "other_charges": "12.123",
	            "amount": "136.082",
	            "discount": "10.123",
	            "currency": "SAR",
	            "reference_no": "ABC-123",
	            "ip_customer": "127.0.0.1",
	            "ip_merchant": "1.1.1.0",
	            "billing_address": "Flat 3021 Manama Bahrain",
	            "city": "Manama",
	            "state": "Manama",
	            "postal_code": "12345",
	            "country": "BHR",
	            "shipping_first_name": "John",
	            "shipping_last_name": "Doe",
	            "address_shipping": "Flat 3021 Manama Bahrain",
	            "state_shipping": "Manama",
	            "city_shipping": "Manama",
	            "postal_code_shipping": "1234",
	            "country_shipping": "BHR",
	            "msg_lang": "English",
	            "cms_with_version": "WordPress4.0-WooCommerce2.3.9"
	            }
	#Creation of Payment Page
	result = paytab.create_payment(**pay_data) #to create payment page, return PaytabsApiResponse with data dict contains payment_url and p_id
	print('Result:', result.data)
	#print("Checkpoint")
	#print("END RESULT:" , paytab.create_payment(**pay_data))
	#print('Result:', result.data) #Result {'result': 'The Pay Page is created.', 'response_code': '4012', 'payment_url': 'https://www.paytabs.com/osdh3SCmEYoD5trKc4oz2VmE91mmQCtqop-PgmsGyFHj9zE/dCetYxYV8qi0XIBl49Y9dMAFPGNTkb6Yot-wgKYKCo94jE8/DTKnWzcrnK65jwoj2X6pmtvj8UI-3YmGDuJ6vDD8FizQOYE/CkdveIWwKhMDPXsuU8vJysaf1ccsOG1XYOZF8O15JInD28z1pER29OEX27E10GXQAI7FCzUJgSyp-6XRgYeejOPf7g', 'p_id': 333348}

	#Verify Payment
	#verifying_data = {
	  #  "payment_reference": result.data['p_id']
	 #}
	#return_obj = paytab.verify_payment(**verifying_data) #verify payment process by using payment reference code, returns PaytabsApiResponse with data dict contains
	#print('Payment Status', return_obj.data) #{"result": "The payment is completed successfully!","response_code": "100","pt_invoice_id": "2124779","amount": 11.45,"currency": "OMR","reference_no": "12","transaction_id": "1720833"} or Raise Exceptions
	return 0


##############################################################

###################### Profile function ######################

@app.route('/profile', methods=['GET', 'POST'])
def profile():
	users = User.query.all()
	plans = Plan2.query.all()

	print("PLANS ARE: ", plans)
	print("Users", users)
	print("length: ", len(users))
	#print("ipn data", ipn_data)
	#payments = Payment.query.all()
	#print("Payments at sucess", payments)
	#print("check inside the payment",payments[1])
	return render_template("profile-page.html", user = users, num=6, plans=plans)

##############################################################

###################### Login function ########################

@app.route('/login', methods=['GET', 'POST'])
def login():
	print_date_time()
	if session['logged_in'] == True:
		print("user is already logged in")
		users = Customer.query.all()
		payments = Payment.query.all()
		plans = Plan4.query.all()
		name = " "
		print(plans)
		return render_template("profile-page.html", users=users, name=name, payments=payments, plans=plans)
	else:
		print("user not logged in")

	return render_template("login-page.html")


@app.route('/customer-login', methods=['GET', 'POST'])
def customerLogin():
	print_date_time()
	if session['logged_in'] == True:
		print("user is already logged in")
		users = User.query.all()
		payments = Payment.query.all()
		plans = Plan2.query.all()
		name = " "
		return render_template("profile-page.html", users=users, name=name, payments=payments, plans=plans)
	else:
		print("user not logged in")

	return render_template("customer-login.html")	


@app.route('/modifyPlan/<int:plan_id>', methods=['GET', 'POST'])
def modifyPlan(plan_id):
	print("Plan ID: " , plan_id)
	plans_object = Plan4.query.filter_by(id=plan_id).first()
	dates = active_dates_for_each_plan(plans_object)
	date1 = plans_object.expiry_date
	date1 = date1 + timedelta(days=1) 

	if plans_object.p_type == "Week": 
		date2 = date1 + timedelta(days=7)
	else:
		date2 = date1 + timedelta(days=30)


	

	print("Date Pause 1: " , date1)
	print("Date Pause 2: " , date2)

	dates2 = active_dates_for_plan(date1 , date2)
	print("Dates2" , date2)
	date1 = date1.strftime('%Y-%#m-%#d')
	print("Date Pause 1: " , date1)

	#return "modify plan" + str(plan_id)
	return render_template("modify-plan.html", plan=plans_object, dates = dates, dates2 = dates2, start_pause_date = date1, plan_id = plan_id)

@app.route('/pausePlan/<int:plan_id>', methods=['GET', 'POST'])
def pausePlan(plan_id):
	#pause = " "
	if request.method == 'POST':
		print("yes post method")
		pasue = request.form["pause"]
		print(request.form["pause"])
		split = request.form["pause"].split('-')
		print(split[0])
		strt = split[0]
		end = split[1]
		split_strt = strt.split('/')
		split_end = end.split('/')
		print("date in details: ")
		print(split_strt[0])
		print(split_strt[1])
		print(split_strt[2])

		date_time_start_obj = datetime.datetime(int(split_strt[2]),int(split_strt[0]),int(split_strt[1]))
		date_time_end_obj = datetime.datetime(int(split_end[2]), int(split_end[0]),int(split_end[1]))
		pause1 = Pause(start_date = date_time_start_obj, expiry_date = date_time_end_obj, plan_id = plan_id)
		db.session.add(pause1)
		db.session.commit()
		pauses = Pause.query.all()
		print("Pause DB objects")
		print(pauses)

		print("date objects: ----->")
		print(date_time_start_obj)
		print(date_time_end_obj)
		




	else:
		print("get method")	
	#unpause = request.form["datepicker2"]
	print("Pausing Dates are:")
	#print(pause)
	#print(unpasue)
	return "hi"

@app.route('/mobile-check', methods=['GET', 'POST'])
def mobileCheck():
	return render_template("mobile-check.html")


@app.route('/who-are-we', methods=['GET', 'POST'])
def whoAreWe():
	return render_template("who-are-we.html")

def updateAdminDetails():
	#def
	print("Inside Update Admin Details function --->")
	#get today's date
	today = date.today()
	tomorrow = today + timedelta(days=1)
	tomorrow = tomorrow.strftime("%Y-%m-%d")
	print("Today's date:", today)
	print("Tomorrow's date:", tomorrow)

	pause_plans = Pause.query.all()
	print("All paused plans: ")
	print(pause_plans)

	for plan in pause_plans: 
		print("Pause plan details:")
		print(plan)
		print(plan.start_date)
		print(plan.plan_id)
		dt = plan.start_date
		dt = dt.strftime("%Y-%m-%d")
		print("Date after trim: ", dt)
		print("Comparison result:")
		print(tomorrow == dt)
		print(type(tomorrow))
		print(type(dt))
		if tomorrow == dt:
			plan_object = Plan4.query.filter_by(id=plan.plan_id).first()
			customer_object = Customer.query.filter_by(mobile=plan_object.customer_mobile).first()

			print(customer_object.name)
			print(customer_object.mobile)

			print("They are equal")
			print("-------->>")
			print("Status of Plan: ", plan_object.is_active)
			if plan_object.is_active == "Active":
				print("inside if statement to make status Pause")
				customer_object.number_of_bags = str(int(customer_object.number_of_bags) - 1)
				customer_object.number_of_plans = str(int(customer_object.number_of_plans) - 1)
				print(customer_object.number_of_bags)
				print(customer_object.number_of_plans)
				plan_object.is_active = "Paused"
				plan_object.p_type = "Week"
				db.session.commit()
				print("-------->>>>>>>>>>")
				print("Status of Plan after commit: ", plan_object.is_active)
				all_plans = Plan4.query.all()
				print("Checking >>>")
				print("Plan 1: ", all_plans[0].is_active)
				print("Plan 2:" , all_plans[1].is_active)




	return True	

@app.route('/updateAdmin', methods=['GET', 'POST'])
def updateAdmin():
	return "Admin Check Applied"

	

@app.route('/mobilre-check', methods=['GET', 'POST'])
def mobileChecrk():
	print_date_time()
	if session['logged_in'] == True:
		print("user is already logged in")
		users = User.query.all()
		payments = Payment.query.all()
		plans = Plan2.query.all()
		name = " "
		return render_template("profile-page.html", users=users, name=name, payments=payments, plans=plans)
	else:
		mobile = request.form["mobile"] 
		session['customer_login_mobile'] = mobile
		customer_object = Customer.query.filter_by(mobile=mobile).first()
		session['logged_in_customer'] = True
		otp_code = generateOTP()
		session['customer_login_otp'] = otp_code
		#for testing purposes
		mobile = session.get('customer_login_mobile')
		customer_object = Customer.query.filter_by(mobile=mobile).first()
		plans_object = Plan4.query.filter_by(customer_mobile=mobile).first()
		plans = Plan4.query.all()
		print(customer_object)
		print(plans_object)
		print(plans)
		print(plans[0])
		customer_plans = []
		customer_plan_dates = []
		for plan in plans:
			if plan.customer_mobile == mobile:
				customer_plans.append(plan)
				plan_dates = active_dates_for_each_plan(plan)
				customer_plan_dates.append(plan_dates)
				print(plan_dates)
				print("plan ID: " , plan.id)
		#uncomment for depeloping purposes
		#sendOTP(mobile, otp_code)
		#print("user not logged in")

	print("Array of plan's dates as follows: ")
	#print(customer_plan_dates[1])
	datpicker_id = 5000	

	return render_template("customer-profile-page.html", users=customer_plans, name=customer_object.name, dates=customer_plan_dates[0], dpid = datpicker_id)




@app.route('/customer-logged-in', methods=['GET', 'POST'])
def customerLoggedIn():
	print_date_time()
	if session['logged_in'] == True:
		print("user is already logged in")
		users = User.query.all()
		payments = Payment.query.all()
		plans = Plan4.query.all()
		name = " "
		return render_template("profile-page.html", users=users, name=name, payments=payments, plans=plans)
	else:
		mobile = request.form["mobile"] 
		session['customer_login_mobile'] = mobile
		customer_object = Customer.query.filter_by(mobile=mobile).first()
		session['logged_in_customer'] = True
		otp_code = generateOTP()
		session['customer_login_otp'] = otp_code
		#for testing purposes
		mobile = session.get('customer_login_mobile')
		customer_object = Customer.query.filter_by(mobile=mobile).first()
		plans_object = Plan4.query.filter_by(customer_mobile=mobile).first()
		plans = Plan4.query.all()
		print(customer_object)
		print(plans_object)
		print(plans)
		print(plans[0])
		customer_plans = []
		customer_plan_dates = []
		for plan in plans:
			if plan.customer_mobile == mobile:
				customer_plans.append(plan)
				plan_dates = active_dates_for_each_plan(plan)
				customer_plan_dates.append(plan_dates)
				print(plan_dates)
				print("plan ID: " , plan.id)
		#uncomment for depeloping purposes
		#sendOTP(mobile, otp_code)
		#print("user not logged in")

	print("Array of plan's dates as follows: ")
	#print(customer_plan_dates[1])
	datpicker_id = 5000	

	return render_template("customer-profile-page.html", users=customer_plans, name=customer_object.name, dates=customer_plan_dates[0], dpid = datpicker_id)


def active_dates_for_plan(start_date, end_date):
	today_date = date.today()


	edate = end_date
	sdate = start_date
	#print("Start Date: ", sdate)
	#print("End Date: ", edate)

	list_of_active_dates = []
	delta = edate.date() - sdate.date()       # as timedelta
	day_name= ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']

	for i in range(delta.days + 1):
		day = sdate  + timedelta(days=i)
		day = day.strftime('%#d-%#m-%Y')
		day_index = datetime.datetime.strptime(day, '%d-%m-%Y').weekday()
		print("day_index: ", day_index)
		if day_index == 4 or day_index == 5:
			print("weekend")
		else:	
			list_of_active_dates.append(day)
		#print(day)
	#print(list_of_date_and_plans)	
	return list_of_active_dates

def active_dates_for_each_plan(plan):
	today_date = date.today()
	edate = plan.expiry_date   # end date
	sdate = plan.start_date	   # start date
	#print("Start Date: ", sdate)
	#print("End Date: ", edate)

	list_of_active_dates = []
	delta = edate.date() - sdate.date()       # as timedelta
	day_name= ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']

	for i in range(delta.days + 1):
		day = sdate  + timedelta(days=i)
		day = day.strftime('%#d-%#m-%Y')
		day_index = datetime.datetime.strptime(day, '%d-%m-%Y').weekday()
		print("day_index: ", day_index)
		if day_index == 4 or day_index == 5:
			print("weekend")
		else:	
			list_of_active_dates.append(day)
		#print(day)
	#print(list_of_date_and_plans)	
	return list_of_active_dates


def sendOTP(mobile, otp_code):
	mob = str(mobile)
	ottp = str(otp_code)
	otp_msg1 = "http://api.smsala.com/api/SendSMS?api_id=API475422013615&api_password=6201620Wg&sms_type=P&encoding=T&sender_id=Vegan%20Dino&phonenumber="+mob
	otp_msg2 = "&textmessage=Your%20OTP%20is%"
	otp_mi="&textmessage=Your OTP is " + ottp
	final_link = otp_msg1 + otp_mi
	otp_req_link = "http://api.smsala.com/api/SendSMS?api_id=API475422013615&api_password=6201620Wg&sms_type=P&encoding=T&sender_id=Vegan%20Dino&phonenumber=" + mob + "&textmessage=Your%20OTP%20is%"+ ottp
	http_req_opt = "http://api.smsala.com/api/SendSMS?api_id=API475422013615&api_password=6201620Wg&sms_type=P&encoding=T&sender_id=Vegan%20Dino&phonenumber=" + mob + "&textmessage=Your%20OTP%20is%" + ottp
	print(otp_mi)
	print(final_link)
	r = requests.get(final_link)

	#sms_message= "Your OTP is " + otp_code
	#print("SMS: ", sms_message)	
	#account_sid = 'AC9d2131f7296e8467f91dc3eccb36fbbb'
	#auth_token = '6f55716b6fcfaa950f1d4c01e5975813'
	#client = Client(account_sid, auth_token)
	#client.messages.create(from_='2062899465',
     #                  to=mobile,
      #                 body=sms_message)

@app.route("/login-otp",methods=['GET', 'POST'])
def loginOTP():
	print(aa)
	print(bb)
	print(cc)
	print(request.form)  
	otp = request.form["otp"]
	otp_gen = session["customer_login_otp"]

	print("generated otp: ", session["otp"])
	print(type(otp_gen))
	print("customer entr otp: ", request.form["otp"])
	print(type(otp))
	print(session["otp"] == int(otp))

	if session["customer_login_otp"] == otp:
		print("OTP matches")
		mobile = session.get('customer_login_mobile')
		customer_object = Customer.query.filter_by(mobile=mobile).first()
		plans_object = Plan4.query.filter_by(customer_mobile=mobile).first()
		plans = Plan4.query.all()
		print(customer_object)
		print(plans_object)
		print(plans)
		print(plans[0])
		customer_plans = []
		for plan in plans:
			if plan.customer_mobile == mobile:
				customer_plans.append(plan)	

		print(customer_plans[0])
		return render_template("customer-profile-page.html", users=customer_plans, name=customer_object.name)
	else:
		return "OTP does not match"


@app.route('/logout', methods=['GET', 'POST'])
def logout():
	session['logged_in'] = False
	print("logging out user from session: ", session['user'])
	return "logged out"	
# Admin customization function
@app.route('/customize', methods=['GET', 'POST'])
def customize():
	price_object = Prices.query.all()
	if request.method == 'POST':
		print("yes post method")
		users = User.query.all()
		payments = Payment.query.all()
		plans = Plan2.query.all()
		print(request.form)  
		price = request.form["price"]  
		price_amount = request.form["price_amount"]
		print("price plan: ", price)
		print("price plan: ", price_amount)
		print("Table result: ", price_object)
		print("Table result: ", price_object[0].amount)
		if price_object == []:
			print("Empty")
			price_db_obj_day = Prices(p_type="Day", amount=0.00)
			price_db_obj_week = Prices(p_type="Week", amount=0.00)
			price_db_obj_month = Prices(p_type="Month", amount=0.00)
			db.session.add(price_db_obj_day)
			db.session.add(price_db_obj_week)
			db.session.add(price_db_obj_month)
			db.session.commit()
		else:
			price_object_required = Prices.query.filter_by(p_type=price).first()
			price_object_required.amount = 	price_amount
			db.session.commit()

		price_object = Prices.query.all()	
		print("Table result after commit: ", price_object)
		print("Table result after commit: ", price_object[0].amount)		

	print("logging out user from session: ", session['user'])
	return render_template("profile-page.html", users=users, payments=payments, plans=plans,
		price_object1=price_object[0].amount, price_object2=price_object[1].amount,price_object3=price_object[2].amount)	

##############################################################

@app.route('/loggingin', methods=['GET', 'POST'])
def logging():
	print_date_time()
	updateAdminDetails()
	print("yes post method")
	status = session.get('logged_in')
	if status == True:
		print("status is True")
		customers = Customer.query.all()
		payments = Payment.query.all()
		plans = Plan4.query.all()
		name = "Mansour Barri"
		return render_template("profile-page.html", users=customers, name=name, payments=payments, plans=plans)
	print(request.form)  
	email = request.form["email"]
	password = request.form["pswd"]
	print("Email: ",email)
	users = User.query.all()
	customers = Customer.query.all()
	payments = Payment.query.all()
	plans = Plan4.query.all()
	print("PLANS ARE: ", plans)
	#payment = payments[0]
	#pay_user = payment.payer_email
	#print("checking payer user:",pay_user)
	print("Users", users)
	user = User.query.filter_by(email=email).first()
	print("check ...", user)
	name = user.name
	if user.email == email:
		print("pass ::", user.password)  
		if user.password == password:
			print("user login authorized.")
			session['user'] = email
			session['logged_in'] = True
			print("session: ", session['user'])
			print("plan status: ")
			print(plans[0].is_active)
			print(type(plans[0].is_active))
			print("plan pauses: ", plans[0].number_of_pauses)
			return render_template("profile-page.html", users=customers, name=name, payments=payments, plans=plans)
			#return redirect(url_for('profile'))
	else:
		print("user login Unauthorized.")	


	return render_template("profile-page.html")

##################################################################################################################

################################### Calculate # of plans in date functions########################################
def dates():
	today_date = date.today()
	sdate = date(2008, 8, 15)   # start date
	edate = date(2021, 1, 1)   # end date
	list_of_date = []
	list_of_plan_frequency = []
	delta = edate - today_date       # as timedelta

	for i in range(delta.days + 1):
		day = today_date + timedelta(days=i)
		#tup = (day,0)
		#dic = {'date' : day, '# plans' : 0}
		#d_f = PlanFrequency(day,0)
		list_of_date.append(day)
		list_of_plan_frequency.append(0)
		#print(day)
	#print(list_of_date_and_plans)
	#print(list_of_date_and_plans)	
	return list_of_date , list_of_plan_frequency

def manipulateDb():
	today_date = date.today()
	end_of_2020 = date(2021, 1, 1)
	for lp in range(100): 
		plan = TestPlan(start_date = today_date, is_active = True, expiry_date = end_of_2020)
		db.session.add(plan)
		db.session.commit()
	
	return 0

def manipulateDb2():
	today_date = date.today()
	end_of_2020 = date(2020, 6, 17)
	plan = TestPlan(start_date = today_date, is_active = True, expiry_date = end_of_2020)
	db.session.add(plan)
	db.session.commit()
	
	return 0	

def activeDatesForEachPlan(plan):
	today_date = date.today()
	edate = plan.expiry_date   # end date
	list_of_active_dates = []
	delta = edate.date() - today_date       # as timedelta

	for i in range(delta.days + 1):
		day = today_date + timedelta(days=i)
		list_of_active_dates.append(day)
		#print(day)
	#print(list_of_date_and_plans)	
	return list_of_active_dates

def activeDatesForAllPlans(plans):
	today_date = date.today()
	#edate = plan.expiry_date   # end date
	list_of_active_dates = []
	#delta = edate.date() - today_date       # as timedelta
	for plan in plans:
		edate = plan.expiry_date   # end date
		delta = edate.date() - today_date       # as timedelta
		for i in range(delta.days + 1):
			day = today_date + timedelta(days=i)
			list_of_active_dates.append(day)
		#print(day)
	#print(list_of_date_and_plans)	
	return list_of_active_dates	


def testDbManipulation():
	list_of_date , list_of_plan_frequency = dates()
	plans = TestPlan.query.all()
	index = 0
	num_iterations = 0
	results = {'date': None, 'freq': None}
	list_of_results = []
	plans_dates = activeDatesForAllPlans(plans)
	#print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
	#print("dates of all plans: ", plans_dates)
	#print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
	#print("dates of calendar: ", list_of_date)
	#print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
	l1 = [date(2021, 1, 1),date(2022, 1, 1),date(2023, 1, 1)]
	l2 = [date(2021, 1, 1),date(2021, 1, 1),date(2021, 1, 1),date(2021, 1, 1),date(2021, 1, 1),date(2021, 1, 1),date(2021, 1, 1),
	date(2022, 1, 1),date(2022, 1, 1),date(2022, 1, 1),date(2023, 1, 1),date(2023, 1, 1)]
	for x in range(len(plans_dates)):
	#print(activeDatesForEachPlan(plans[0]))
		#dates_of_active_plan = activeDatesForEachPlan(plans[x])
		results = {'date': None, 'freq': None}
		results['date'] = plans_dates[x]
		results['freq'] = list_of_date.count(plans_dates[x])
		#print("frequency: ", results['freq'])
		list_of_results.append(results)

	newList = Counter(plans_dates)

	for k,v in newList.items():
		if v > 100:
			m = 1
	return newList


##################################################################################################################	



##################### Database functions #####################

class User(db.Model):
	email = db.Column(db.String(50), primary_key=True)
	name = db.Column(db.String(50))
	admin = db.Column(db.Boolean, default=False)
	password = db.Column(db.String(50))
	payments = db.relationship('Payment', backref='user',
                                lazy='dynamic')
	plan = db.relationship("Plan2", uselist=False, backref='user')

	def __init__(self,email,name,admin, password,payments = [], plan = []):
		self.email = email
		self.name = name
		self.admin = admin
		self.password = password
		self.payments = payments


class Customer(db.Model):
	mobile = db.Column(db.String(50), primary_key=True)
	name = db.Column(db.String(50))
	number_of_plans = db.Column(db.String(50))
	number_of_bags = db.Column(db.String(50))
	special_customer = db.Column(db.String(50))
	address = db.Column(db.String(50))
	delivery_option = db.Column(db.Boolean, default=False)
	plan = db.relationship("Plan4", uselist=True, backref='customer')

	def __init__(self,mobile,name,number_of_plans, number_of_bags,special_customer, address,
	delivery_option, plan = []):
		self.mobile = mobile
		self.name = name
		self.number_of_plans = number_of_plans
		self.number_of_bags = number_of_bags
		self.special_customer = special_customer
		self.address = address
		self.delivery_option = delivery_option
		self.plan = plan

class Pause(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	start_date = db.Column(db.DateTime)
	expiry_date = db.Column(db.DateTime)
	plan_id = db.Column(db.String(50), db.ForeignKey('plan4.id'))

class Plan4(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	customer_mobile = db.Column(db.String(50), db.ForeignKey('customer.mobile'))
	customer_name = db.Column(db.String(50))  
	start_date = db.Column(db.DateTime)
	p_type = db.Column(db.String(50))
	is_active = db.Column(db.String(50))
	expiry_date = db.Column(db.DateTime)
	number_of_pauses= db.Column(db.Integer)
	pause = db.relationship("Pause", uselist=True, backref='plan4')
	

class Plan3(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	customer_mobile = db.Column(db.String(50), db.ForeignKey('customer.mobile')) 
	start_date = db.Column(db.DateTime)
	p_type = db.Column(db.String(50))
	is_active = db.Column(db.Boolean, default=False)
	expiry_date = db.Column(db.DateTime)	





class Payment(db.Model):
	payment_id = db.Column(db.String(50), primary_key=True)
	payment_date = db.Column(db.String(50))
	payment_amount = db.Column(db.Float)
	payment_status = db.Column(db.String(50))
	payer_paypal_email = db.Column(db.String(50))
	payer_start_date = db.Column(db.String(50))
	payer_plan = db.Column(db.String(50))
	payer_email = db.Column(db.String(50),db.ForeignKey('user.email'))
	plan = db.relationship("Plan2", uselist=False, backref="plan")


class Plan(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True) 
	email = db.Column(db.String(50), db.ForeignKey('user.email'))
	payment_id = db.Column(db.String(50), db.ForeignKey('payment.payment_id'))
	start_date = db.Column(db.DateTime)
	p_type = db.Column(db.String(50))
	is_active = db.Column(db.Boolean, default=False)
	delivery_option = db.Column(db.String(50))

class Plan1(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True) 
	email = db.Column(db.String(50), db.ForeignKey('user.email'))
	payment_id = db.Column(db.String(50), db.ForeignKey('payment.payment_id'))
	start_date = db.Column(db.DateTime)
	p_type = db.Column(db.String(50))
	is_active = db.Column(db.Boolean, default=False)
	delivery_option = db.Column(db.String(50))
	expiry_date = db.Column(db.DateTime)

class Plan2(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True) 
	email = db.Column(db.String(50), db.ForeignKey('user.email'))
	payment_id = db.Column(db.String(50), db.ForeignKey('payment.payment_id'))
	start_date = db.Column(db.DateTime)
	p_type = db.Column(db.String(50))
	is_active = db.Column(db.Boolean, default=False)
	delivery_option = db.Column(db.String(50))
	expiry_date = db.Column(db.DateTime)	

class TestPlan(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True) 
	start_date = db.Column(db.DateTime)
	is_active = db.Column(db.Boolean, default=False)
	expiry_date = db.Column(db.DateTime)	


class Prices(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True) 
	p_type = db.Column(db.String(50))
	amount = db.Column(db.Float)		
	#payment = db.relationship("Payment", back_populates="plan")                           	
	#user = db.relationship("User", back_populates="plan")                            	

##############################################################		  				   

if __name__ == "__main__":
    app.run(debug=True)



