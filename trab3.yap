:- op(100,xfy,:).
:- use_module(library(lists)).

timetable(edinburgh,london,
[ 9:40/10:50/ba4733/alldays,
13:40/14:50/ba4773/alldays,
19:40/20:50/ba4833/[mo,tu,we,th,fr,su]]).
timetable(london,edinburgh,
[ 9:40/10:50/ba4732/alldays,
11:40/12:50/ba4752/alldays,
18:40/19:50/ba4822/[mo,tu,we,th,fr]]).
timetable(london,ljubljana,
[13:20/16:20/ju201/[fr],
13:20/16:20/ju213/[su]]).n
timetable(london,zurich,
[ 9:10/11:45/ba614/alldays,
14:45/17:20/sr805/alldays]).
timetable(london,milan,
[ 8:30/11:20/ba510/alldays,
11:00/13:50/az459/alldays]).
timetable(ljubljana,zurich,
[11:30/12:40/ju322/[tu,th]]).
timetable(ljubljana,london,
[11:10/12:20/yu200/[fr],
11:25/12:20/yu212/[su]]).
timetable(milan,london,
[ 9:10/10:00/az458/alldays,
12:20/13:10/ba511/alldays]).
timetable(milan,zurich,
[ 9:25/10:15/sr621/alldays,
12:45/13:35/sr623/alldays]).
timetable(zurich,ljubljana,
[13:30/14:40/yu323/[tu,th]]).
timetable(zurich,london,
[ 9:00/9:40/ba613/[mo,tu,we,th,fr,sa],
16:10/16:55/sr806/[mo,tu,we,th,fr,su]]).
timetable(zurich,milan,
[ 7:55/8:45/sr620/alldays]).

flight(Place1,Place2,Day,Flight_num,Dep_time,Arr_time):-
    timetable(Place1,Place2,List_of_flights),
    member(Dep_time/Arr_time/Flight_num/List_of_days, List_of_flights),
    existDayFlight(Day,List_of_days).

existDayFlight(Day,alldays) :- 
    member(Day,[mo,tu,we,th,fr,sa,su]).
existDayFlight(Day,List_of_days) :- 
    member(Day,List_of_days).

transfer(Hour1:Minutes1 , Hour2:Minutes2) :-
    (Minutes2 - Minutes1) + (Hour2 - Hour1)*60 >= 40.

route(Place1,Place1,_,_).
route(Place1,Place2, Day, Path) :-
	path(Place1,Place2,Day,[Place1],Path).

path(Place1,Place2,Day,Visited,[Place1:Place2:Day:Flight_num:Dep_time:Arr_time]) :-
	flight(Place1,Place2,Day,Flight_num,Dep_time,Arr_time).

path(Place1,Place2,Day, Visited,Path) :-
	flight(Place1,Connection,Day,Flight_num,Dep_time,Arr_time),						
	not member(Connection,Visited),													
	path(Connection,Place2,Day,[Connection|Visited],NextPath),						
	append([Place1:Connection:Day:Flight_num:Dep_time:Arr_time],NextPath,Path),
	checkTime(Path).															

arrivalTime(_:_:_:_:(_):(ArrivalHour), ArrivalHour).
depTime(_:_:_:(_):(DepHour):_, DepHour).

checkTime([]).
checkTime([_]).
checkTime([Flight1, Flight2 | XS]) :-
	arrivalTime(Flight1,ArrivalHour),
	depTime(Flight2,DepHour),
	transfer(ArrivalHour,DepHour),
	checkTime([Flight2|XS]).

next_day(mo,tu).
next_day(tu,we).
next_day(we,th).
next_day(th,fr).
next_day(fr,sa).
next_day(sa,su).
next_day(su,mo).


travel(City,Destinations,IniDay,EndDay,[City:Connection:IniDay:Number:DepartureTime:ArrivalTime|Remaining]) :-
	permutation(Destinations,AllDestinations),
	member(Connection,AllDestinations),
	flight(City,Connection,IniDay,Number,DepartureTime,ArrivalTime),
	next_day(IniDay,ActualDay),
	delete(AllDestinations,Connection,Destinations2),
	itinerary(Connection,Destinations2,City,ActualDay,EndDay,Remaining).

itinerary(_,_,_,IniDay,IniDay,_) :- false.

itinerary(City,[],EndCity,IniDay,EndDay,[City:EndCity:IniDay:Number:DepartureTime:ArrivalTime]) :-
	flight(City,EndCity,IniDay,Number,DepartureTime,ArrivalTime).

itinerary(City,Destinations,EndCity,IniDay,EndDay,[City:Connection:IniDay:Number:DepartureTime:ArrivalTime|Remaining]) :-
	member(Connection,Destinations),
	flight(City,Connection,IniDay,Number,DepartureTime,ArrivalTime),
	next_day(IniDay,ActualDay),
	delete(Destinations,Connection,Destinations2),
	itinerary(Connection,Destinations2,EndCity,ActualDay,EndDay,Remaining).