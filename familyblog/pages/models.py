from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Page(models.Model):
    title = models.CharField(max_length=255)    
    title_tag = models.CharField(max_length=255, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(blank=True, null=True)   
    
    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home', args=(self.id,))

# Create your models here.
