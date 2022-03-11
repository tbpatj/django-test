from django.db import models
from datetime import time

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=200)
    floor_number = models.IntegerField(default=1)
    room_number = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.name}: room {self.room_number} on floor {self.floor_number}"

class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
    #adds a foriegn key, we need to specify the on delete behavior, cascade just tells us that if a room gets deleted all of the rest of the meetings in that orom wil be deleted as well
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return\
            f"{self.title} at {self.start_time} on {self.date}";