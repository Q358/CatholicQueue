from django.db import models

# from django.utils import timezone
# date = models.DateTimeField(default=timezone.now)

class Hour(models.Model):
    lineLength = models.IntegerField()
    busynessLevel = models.CharField(max_length=100)
    isCurrent = models.BooleanField()

    # Shows what will show up when queried
    def __str__(self):
        return self.busynessLevel

class Day(models.Model):
    month = models.IntegerField()
    day = models.IntegerField()
    dayOfWeek = models.IntegerField()

class Week(models.Model):
    weekStartDay = models.ForeignKey(Day, on_delete=models.CASCADE)
