from datetime import datetime

import pytz
from djongo import models


# Create your models here.
TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))

class User(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    timezone = models.CharField(max_length=32, choices=TIMEZONES,default='UTC')
    login_time = models.DateTimeField(default=datetime.now())
    logout_time = models.DateTimeField(default=datetime.now())
    def __str__(self):
        return self.name
