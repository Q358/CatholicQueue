# herokun run lineincrementer.py
from time import perf_counter
from tracemalloc import start
from test_app.models import Queue, Hour, Day, Week, Month
from datetime import *

clock = time.CLOCK_REALTIME
startTime = None
line = Queue.objects.first()
currentHour = Hour.objects.filter(isCurrent=True).first()
line = currentHour.lineLength
openTime = 10
closeTime = 17

while(1==1):
	if(date.weekday >= 5 or clock.time < openTime or clock.time > closeTime):
		line = 0
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
				startTime = clock.minute
			else if(time.perf_counter() - time.):
				
			# Sets busynessLevel - might be better to do this in the html
			#setBusyness(currentHour, line)
		if(buttonPushed):
			currentHour = Hour.objects.filter(isCurrent=True).first()
			currentHour.lineLength += 1
			currentHour.save()


def setBusyness(hour, line):
	hour.busynessLevel = "Basically Empty"
	if(line > 3):
		hour.busynessLevel = "Not That Busy"
		if(line > 5):
			hour.busynessLevel = "Somewhat Busy"
			if(line > 7):
				hour.busynessLevel = "Busy"
				if(line > 10):
					hour.busynessLevel = "Absolutely Packed"