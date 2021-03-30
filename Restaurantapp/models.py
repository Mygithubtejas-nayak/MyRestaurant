from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(default=None)
    mobile_number = models.CharField(max_length=100 ,default=None)
    body = models.TextField()

    def __str__(self):
        return self.name