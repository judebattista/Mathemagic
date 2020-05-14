from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# For more info on fields and field types: https://docs.djangoproject.com/en/3.0/ref/models/fields/#model-field-types
class Meeting(models.Model):
    date = models.DateField() # Python datetime.date instance
    startTime = models.TimeField() # Python datetime.time instance
    endTime = models.TimeField() # Python datetime.time instance
    title = models.CharField(max_length=120)
    description = models.TextField()
    people = models.ManyToManyField(User)
    
    def __str__(self):
        return "You haven't implemented the string funciton yet silly"

