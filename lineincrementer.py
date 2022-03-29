from test_app.models import Hour
from datetime import *
clock = time.CLOCK_REALTIME
currentHour = Hour.objects.filter(isCurrent=True).first()
line = currentHour.lineLength

while(1==1):
	if(clock.hour != currentHour.hourOfDay):
		# Makes a new hour object
		currentHour.isCurrent = False
		currentHour.save()
		currentHour = Hour(lineLength = line, busynessLevel = "Is Basically Empty", isCurrent = True, hourOfDay = clock.hour)
		currentHour.save()
	line = currentHour.lineLength
	if(line > 0):
		# Starts decrementing lineLength every 5 mins
		timer
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