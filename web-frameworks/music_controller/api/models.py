from django.db import models
import string
import random

def generate_room_code():
    length = 6
   
    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Room.objects.filter(code=code).count() == 0:
            break
    return code

# Create your models here.
class Room(models.Model):
    code = models.CharField(max_Length=8, default="", unique=True)
    host = models.CharField(max_Length=50, unique=True)
    guest_can_pause = models.BooleanField(null=false, default=False)
    votes_to_skip = models.IntegerField(null=False, Default=1)
    created_at = models.DateTimeField(auto_now_add=True)
