# import imp
from postalservice.wsgi import *
from test_app.models import Hour, Queue

currentHour = Hour.objects.filter(isCurrent=True).first()
currentHour.lineLength += 1
currentHour.save()
queue = Queue.objects.first()
queue.length += 1
queue.save()
print("Line +1")