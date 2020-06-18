	for y in range(len(plans)):
		#index = 0
		for x in range(len(list_of_date)):
			#print("X value: ", x)
			dates_of_active_plan = activeDatesForEachPlan(plans[y])
			#print("Single **Active dates for plan are: ", dates_of_active_plan[0])
			#print("Active dates for plan are: ", dates_of_active_plan)
			#print("My object: ", list_of_date_and_plans[0])
			#if dates_of_active_plan[y] == list_of_date_and_plans[x].date:
				#print("Got inside if stmt")

			#print("1st date: ", dates_of_active_plan[y])
			#print("2nd date: ", list_of_date_and_plans[x].date)
			#print("dic value before start: " , list_of_date_and_plans[0].frequency)		
			if dates_of_active_plan[y] == list_of_date[x]:
				print("they are equal")
				#p_numbers= list_of_date_and_plans[x].frequency
				#p_numbers = p_numbers + 1
				index = index + 1
				print("index: ", index)
				list_of_plan_frequency[x] = list_of_plan_frequency[x] + 1
				print("Freq: ", list_of_plan_frequency[x])
				#print(dates_of_active_plan[y])
				#print(list_of_date_and_plans[x])
			#else:
				#print("they are not equal")
				#m=0
				#print(dates_of_active_plan[y])
				#print(list_of_date_and_plans[x].date)
		#print("#" + str(index) + " , " + x)
		#index= index+1
			#print(x)
	#print(list_of_date_and_plans)
	print("################################")
	#print(list_of_date_and_plans[0])
	#print(list_of_date_and_plans[1])
	#print("p_number: ", p_numbers)
	print("dic value: " , list_of_plan_frequency)
	print("*****************************************************")
	#print("num of iterations is: ", num_iterations)
	
	
	#print("index: ", index)
	




	def testDbManipulation():
	list_of_date , list_of_plan_frequency = dates()
	plans = TestPlan.query.all()
	index = 0
	num_iterations = 0
	results = {'date': None, 'freq': None}
	list_of_results = []

	l1 = [date(2021, 1, 1),date(2022, 1, 1),date(2023, 1, 1)]
	l2 = [date(2021, 1, 1),date(2021, 1, 1),date(2021, 1, 1),date(2021, 1, 1),date(2021, 1, 1),date(2021, 1, 1),date(2021, 1, 1),
	date(2022, 1, 1),date(2022, 1, 1),date(2022, 1, 1),date(2023, 1, 1),date(2023, 1, 1)]
	for x in range(len(l1)):
	#print(activeDatesForEachPlan(plans[0]))
		#dates_of_active_plan = activeDatesForEachPlan(plans[x])
		results = {'date': None, 'freq': None}
		results['date'] = l1[x]
		results['freq'] = l2.count(l1[x])
		list_of_results.append(results)



	#print("New plan dates: ", dates_of_active_plan)
	#print("First plan" , dates_of_active_plan)
	print("*********************************************************************************")
	print("*********************************************************************************")
	print("dictionary frequency: ", results)
	print("list of dic: ", list_of_results)

	#print("list of dates: ", list_of_date)
	print("*********************************************************************************")
	print("*********************************************************************************")
	print("list of frequencies: ", list_of_plan_frequency)
	print("list of frequencies length: ", len(list_of_plan_frequency))
	print("list of dates length: ", len(list_of_date))



	return 0


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


	#print("New plan dates: ", dates_of_active_plan)
	#print("First plan" , dates_of_active_plan)
	#print(Counter(plans_dates))
	newList = Counter(plans_dates)
	#print("*********************************************************************************")
	#print("*********************************************************************************")
	#print("*********************************************************************************")
	#print("*********************************************************************************")

	for k,v in newList.items():
		if v > 100:
			#print(k,v)
	#print("*********************************************************************************")
	#print("*********************************************************************************")
	#print("dictionary frequency: ", results)
	#print("list of dic: ", list_of_results)

	#print("list of dates: ", list_of_date)
	#print("*********************************************************************************")
	#print("*********************************************************************************")
	#print("list of frequencies: ", list_of_plan_frequency)
	#print("list of frequencies length: ", len(list_of_plan_frequency))
	#print("list of dates length: ", len(list_of_date))
	return newList