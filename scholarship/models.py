from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Category (models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Scholarship (models.Model):
    title = models.CharField(max_length=100)
    status = models.CharField(max_length=10)
    institution = models.CharField(max_length=100)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    # author = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

class Application (models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    scholarship = models.ForeignKey(Scholarship, on_delete=models.PROTECT, null=True)
    accepted = models.BooleanField(null=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} {self.scholarship.title}'
