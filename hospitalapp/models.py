from django.db import models

# Create your models here.

class Users(models.Model):
    fullname = models.CharField(max_length=200)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    age = models.IntegerField(null=True)
    password = models.CharField(max_length=50)
    date = models.DateTimeField(null=True)

    def __str__(self):
        return self.fullname

class Products(models.Model):
    product_name = models.CharField(max_length=300)
    product_price = models.CharField(max_length=100)
    product_quantity = models.IntegerField()

    def __str__(self):
        return self.product_name

class Member(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.username

class Appointment(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=100)
    date = models.DateTimeField(null=True)
    department = models.CharField(max_length=100)
    doctor = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name

class ImageModel(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50)
    price = models.CharField(max_length=50)