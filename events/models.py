from django.utils import timezone

from django.db import models


class Events(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    Location = models.CharField(max_length=200)
    description = models.TextField(null=True, max_length=12)
    created_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
