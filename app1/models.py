import pytz
from django.db import models

TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    timezone = models.CharField(max_length=32, choices=TIMEZONES, default='UTC')

    def __str__(self):
        return self.name



class Activity(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    log_in = models.DateTimeField(null=True, blank=True)
    log_out = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.user.name