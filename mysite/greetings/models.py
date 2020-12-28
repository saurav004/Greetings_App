from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


class GreetingClass(models.Model):
    Greeting_Title = models.CharField(max_length=30)
    message = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    greeting_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.author}  | {self.Greeting_Title}"

    @staticmethod
    def get_absolute_url():
        return reverse('greetings_home')

