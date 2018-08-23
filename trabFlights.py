class Flight():
	def __init__(self, place1, place2, departure, arrival, flight_num, days):
		self.place1 = place1
		self.place2 = place2
		dep_time = departure.split(":")
		self.departure = eval(dep_time[0]) * 60 + eval(dep_time[1])
		arr_time = arrival.split(":")
		self.arrival = eval(arr_time[0]) * 60 + eval(arr_time[1])
		self.days = days
		self.flight_num = flight_num

alldays = ['mo', 'tu', 'we', 'th', 'fr', 'sa', 'su']
timetable = []
timetable.append(Flight("edinburgh", "london", "9:40", "10:50", 'ba4733', alldays))
timetable.append(Flight("edinburgh", "london", "13:40", "14:50", 'ba4773', alldays))
timetable.append(Flight("edinburgh", "london", "19:40", "20:50", 'ba4833', ["mo","tu","we","th","fr","su"]))
timetable.append(Flight("london", "edinburgh", "9:40","10:50","ba4732", alldays))
timetable.append(Flight("london", "edinburgh", "11:40", "12:50", "ba4752", alldays))
timetable.append(Flight("london", "edinburgh", "18:40", "19:50", "ba4822", ["mo","tu","we","th","fr"]))
timetable.append(Flight("london", "ljubljana", "13:20", "16:20", "ju201", ["fr"]))
timetable.append(Flight("london", "ljubljana", "13:20", "16:20", "ju213", ["su"]))
timetable.append(Flight("london", "zurich", "9:10", "11:45", "ba614", alldays))
timetable.append(Flight("london", "milan", "8:30", "11:20", "ba510", alldays))
timetable.append(Flight("london", "milan", "11:00", "13:50", "az459", alldays))
timetable.append(Flight("ljubljana", "zurich", "11:30", "12:40", "ju322", ["tu","th"]))
timetable.append(Flight("ljubljana", "london", "11:10", "12:20", "yu200", ["fr"]))
timetable.append(Flight("ljubljana", "london", "11:25", "12:20", "yu212", ["su"]))
timetable.append(Flight("milan", "london", "9:10", "10:00", "az458", alldays))
timetable.append(Flight("milan", "london", "12:20", "13:10", "ba511", alldays))
timetable.append(Flight("milan", "zurich", "9:25", "10:15", "sr621", alldays))
timetable.append(Flight("milan", "zurich", "12:45", "13:35", "sr623", alldays))
timetable.append(Flight("zurich", "ljubljana", "13:30", "14:40", "yu323", ["tu","th"]))
timetable.append(Flight("zurich", "london", "9:00", "9:40", "ba613", ["mo","tu","we","th","fr","sa"]))
timetable.append(Flight("zurich", "london", "16:10", "16:55", "sr806", ["mo","tu","we","th","fr","su"]))
timetable.append(Flight("zurich", "milan", "7:55", "8:45", "sr620", alldays))

def inputDay(string):
	print()
	for i, day in enumerate(alldays):
		print(i,"-", day)
	return alldays[eval(input(string))]

def availableFlights(departure, destination, day, time, flights):
	flag = False
	for tt in timetable:
		if tt.place1 == departure and day in tt.days and tt.departure > time:
			if tt.place2 == destination:
				flights.insert(0, None)
				flights.insert(0, tt)
				flag = True
			elif availableFlights(tt.place2, destination, day, tt.arrival, flights):
				flights.insert(0, tt)
				flag = True
	return flag

def nextDay(day):
	index = alldays.index(day)
	if index > len(alldays):
		index = 0
	return alldays[index]

def searchRoutes(place, place_end, start_day, end_day, places, route, flights):
	flag = False
	if start_day == end_day:
		return False 
	if places == []:
		for tt in timetable:
			if tt.place1 == place and tt.place2 == place_end and end_day in tt.days:
				flights.append(None)
				for cf in route:
					flights.append(cf)
				flights.append(tt)
				flag = True
	else:
		for tt in timetable:
			if tt.place1 == place and tt.place2 in places and start_day in tt.days:
				places.remove(tt.place2)
				route.append(tt)
				if searchRoutes(tt.place2, place_end, nextDay(start_day), end_day, places, route, flights):
					flag = True
				route.remove(tt)
				places.append(tt.place2)
	if flag:
		return flag
	else:
		return searchRoutes(place, place_end, nextDay(start_day), end_day, places, route, flights)

val = eval(input("1 - In which days of the week there is a direct flight from Place1 to Place2?\n2 - What are the available flights from Place1 to Place2 on a day?\n3 - I need to visit cities C1, C2 and C3, starting my flight in city S on Tuesday and returning to S on Friday. In which sequence I should visit cities C1, C2 and C3 so that I don’t need to have more than one flight a day?\n"))
if val == 1:
	place1 = input("Place 1: ")
	place2 = input("Place 2: ")
	days = []
	for tt in timetable:
		if tt.place1 == place1 and tt.place2 == place2:
			days += tt.days
	print(set(days))
elif val == 2:
	place1 = input("Place 1: ")
	place2 = input("Place 2: ")
	day = inputDay("\nDay: ")
	flights = []
	availableFlights(place1, place2, day, 0, flights)
	for f in flights:
		if f == None:
			print()
		else:
			print(f.place1, f.place2, f.flight_num)
elif val == 3:
	place1 = input("Departure: ")
	places = []
	inp = input("Digite as cidades a visitar, escreva 0 quando acabar de inserir:\n")
	while inp != "0":
		places.append(inp)
		inp = input()
	start_day = inputDay("Start Day: ")
	end_day = inputDay("End Day: ")
	flights = []
	searchRoutes(place1, place1, start_day, end_day, places, [], flights)
	for f in flights:
		if f == None:
			print()
		else:
			print(f.place1, f.place2, f.flight_num)