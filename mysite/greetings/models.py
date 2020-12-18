from django.db import models
from django.contrib.auth.models import User


# Create your models here.
from django.urls import reverse


class GreetingClass(models.Model):
    Greeting_Title = models.CharField(max_length=30)
    message = models.TextField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return f"{self.author}  | {self.Greeting_Title}"

    def get_absolute_url(self):
        return reverse('greetings_home')
        # return reverse('SingleGreeting', args=(str(self.id)))

