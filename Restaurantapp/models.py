from django.db import models

# Create your models here.
class ContactUS(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(default=None)
    mobile_number = models.CharField(max_length=100 ,default=None)
    Query = models.TextField()

    def __str__(self):
        return self.name