from django.db import models
from django.utils import timezone

class ToDolist(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    to_date = models.DateTimeField(default=timezone.now)


