from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)

    title = models.CharField(max_length=20, blank=False)
    caption = models.TextField(max_length=255)
    flyer = models.FileField(upload_to='flyer', null=False, blank=False)
    event_date = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=150, default='', blank=True, null=True)
    category = models.CharField(max_length=255, default='')
    created_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('posts:home')

    def __str__(self):
        return f"@{self.user}'s Post"

    class Meta:
        ordering = ['-created_at']
        unique_together = ['title']

class Category(models.Model):
    name = models.CharField(max_length=150, null=True, blank=False)

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return f"Category: {self.name}"

    def get_absolute_url(self):
        return reverse('posts:home')

    class Meta:
        ordering = ['name']