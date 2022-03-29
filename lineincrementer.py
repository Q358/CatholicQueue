from test_app.models import Hour
from datetime import *
clock = time.CLOCK_REALTIME

while(1=1)
	if(buttonPushed)
		currentHour = Hour.objects.filter(isCurrent=True).first()
		currentHour.lineLength += 1
		currentHour.save()
	if(clock.hour != currentHour.hourOfDay)
		#make new hour object
	if(currentHour.lineLength > 0)
		#start decrementing lineLength every 5 mins