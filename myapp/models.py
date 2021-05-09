from django.db import models
from django.core.files.storage import FileSystemStorage

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    password = models.CharField(max_length=500)
    category = models.CharField(max_length=500)

    def __str__(self):
        return '{}'.format(self.name)


class Property(models.Model):
    owner = models.CharField(max_length=500, null=True)
    number_and_street = models.CharField(max_length=500, null=True)
    pincode = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)
    occupied = models.CharField(max_length=100, null=True)
    rent = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    notes = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.owner+"\'s property"


class Image(models.Model):

    post = models.ForeignKey(Property, default=None, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='static/images/')