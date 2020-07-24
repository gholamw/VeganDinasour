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
	print("customer entr otp: ", request.form["otp"])
	print(type(otp))
	print(session["otp"] == int(otp))
	if session["otp"] == otp:
		print("OTP matches")
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
		customer = Customer(mobile=customer_mobile, name=customer_name,number_of_plans = toatl_number_of_plans,
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
			plan = Plan4(customer_mobile=customer_mobile, customer_name = customer_name,  start_date=date, p_type = "Day", is_active = True, expiry_date= date, customer = customer)
			db.session.add(plan)

		#for loop for Week 
		for i in range(week_plans):
			plan = Plan4(customer_mobile=customer_mobile, customer_name = customer_name, start_date=date, p_type = "Week", is_active = True, expiry_date= date, customer = customer)
			db.session.add(plan)

		#for loop for Month 
		for i in range(month_plans):
			plan = Plan4(customer_mobile=customer_mobile, customer_name = customer_name, start_date=date, p_type = "Month", is_active = True, expiry_date= date, customer = customer)
			db.session.add(plan)	
		db.session.commit()
	

		return render_template('paypal.html', email=aa, amount = bb, plan = cc)
		#return "Two way authentication approved"
	return "Two way authentication denied"	