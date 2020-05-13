from django.conf import settings
from django.db import models
from django.utils import timezone
from random import choice
colors = ["red_note", "green_note", "blue_note", "purple_note", "yellow_note"]

class Note(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    color = models.CharField(max_length=30, default=choice(colors))
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
