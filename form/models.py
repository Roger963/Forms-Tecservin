import datetime
from django.db import models

class survey_page (models.Model):
    message = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    gender = models.CharField(max_length=200)
    date = models.DateTimeField(default=datetime.datetime.now)
