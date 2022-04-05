import imp
from postalservice.wsgi import *
from test_app.models import Hour

currentHour = Hour.objects.filter(isCurrent=True).first()
currentHour.lineLength += 1
currentHour.save()
print("Line +1")