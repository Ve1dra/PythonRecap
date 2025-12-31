from django.db import models

# Create your models here.
class Table(models.Model):
    #Event, envent duration, starttime, endtime and event venue
    event = models.CharField(max_length=100)
    duration = models.CharField(max_length=20)
    starts = models.CharField(max_length=30)
    ends = models.CharField(max_length=30)
    venue = models.CharField(max_length=100)

    def __str__(self):
        return (f"ID: {self.id} Event: {self.event} Duration: {self.duration} Starts: {self.starts} Ends: {self.ends} Venue: {self.venue}")
    