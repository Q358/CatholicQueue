# heroku run lineincrementer.py
from postalservice.wsgi import *
from time import *
from tracemalloc import start
from test_app.models import Queue, Hour, Day, Week, Month
#from datetime import *

clock = time.clock_gettime(0)
startTime = None
queue = Queue.objects.first()
currentHour = Hour.objects.filter(isCurrent=True).first()
line = currentHour.lineLength
openTime = 10
closeTime = 17

while(1==1):
	# If the post office is not open, the current hour is frozen as 
	if(date.weekday >= 5 or clock.hour < openTime or clock.hour > closeTime):
		queue.length = 0
		queue.save()
		currentHour.isOpen = False
	else:
		if(clock.hour != currentHour.hourOfDay):
			# Makes a new hour object
			currentHour.isCurrent = False
			currentHour.save()
			currentHour = Hour(lineLength = line, busynessLevel = "Is Basically Empty", isCurrent = True, hourOfDay = clock.hour)
			currentHour.save()
		line = currentHour.lineLength
		if(line > 0):
			# Starts decrementing lineLength every 5 mins
			if(startTime == None):
				startTime = time.perf_counter()
			elif(time.perf_counter() - startTime >= 5): # needs to be fixed at some point
				print("Line -1")
			# Sets busynessLevel - might be better to do this in the html
			#setBusyness(currentHour, line)

# def setBusyness(hour, line):
# 	hour.busynessLevel = "Basically Empty"
# 	if(line > 3):
# 		hour.busynessLevel = "Not That Busy"
# 		if(line > 5):
# 			hour.busynessLevel = "Somewhat Busy"
# 			if(line > 7):
# 				hour.busynessLevel = "Busy"
# 				if(line > 10):
# 					hour.busynessLevel = "Absolutely Packed"