from django.db import models

# from django.utils import timezone
# date = models.DateTimeField(default=timezone.now)

class Queue(models.Model):
    length = models.IntegerField()

class Hour(models.Model):
    lineLength = models.IntegerField()
    #busynessLevel = models.CharField(max_length=100)
    isCurrent = models.BooleanField()
    hourOfDay = models.IntegerField()
    isOpen = models.BooleanField()

    # Shows what will show up when queried
    def __str__(self):
        return str(self.hourOfDay)

class Day(models.Model):
    month = models.IntegerField()
    day = models.IntegerField()
    dayOfWeek = models.IntegerField()

class Week(models.Model):
    days = [models.ForeignKey(Day, on_delete=models.CASCADE)]

class Month(models.Model):
    weeks = [models.ForeignKey(Week, on_delete=models.CASCADE)]

class Post(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to = 'images/')

def __str__(self):
    return self.title