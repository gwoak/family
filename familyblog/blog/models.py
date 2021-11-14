from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# class to convert user input to lower case for new categories
class NameField(models.CharField):
    def __init__(self, *args, **kwargs):
        super(NameField, self).__init__(*args, **kwargs)

    def get_prep_value(self, value):
        return str(value).lower()

class Category(models.Model):
    name = NameField(max_length=255)

    def __str__(self):
       return self.name

    def get_absolute_url(self):
       return reverse('post_detail', args=(str(self.id)))

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile")
    website_url = models.CharField(max_length=255, null=True, blank=True)
    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user)


class Post(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    title_tag = models.CharField(max_length=255, default='Stories')
    category = models.CharField(max_length=255, default='uncategorised')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    snippet = models.CharField(max_length=255)
    body = models.TextField(blank=True, null=True)   
    date_created = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('post_detail', args=(self.id,))
# Create your models here.
