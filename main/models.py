from django.db import models
from django.db.models.base import Model
from django.db.models.expressions import F

# Create your models here.
class Todo(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)


class ToMeet(models.Model):
    persone = models.CharField(max_length=100)
    date_of_meeting = models.DateField(auto_now_add=False)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

class Habits(models.Model):
    name = models.CharField(max_length=100)
    done_for_today = models.BooleanField(default=False)
    important = models.BooleanField(default=False)
    comment = models.TextField()