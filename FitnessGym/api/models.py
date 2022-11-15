from django.db import models
from django.contrib.auth.models import AbstractUser


GENDER = {
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Others')
}

class User(AbstractUser):

    first_name = models.CharField(max_length=175)
    last_name = models.CharField(max_length=175)
    username = models.EmailField(max_length=175, unique=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    phone = models.CharField(max_length=10, blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER, blank=True, null=True)
    session_token = models.CharField(max_length=30, default=0)
    created_at = models.DateTimeField(auto_now=True)
    updates_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.email}'


class Enquiry(models.Model):

    name = models.CharField(max_length=120)
    contactNO = models.CharField(max_length=10)
    emailID = models.EmailField(max_length=120)
    age = models.CharField(max_length= 20 )
    gender = models.CharField(max_length=1, choices=GENDER)
    context = models.TextField(max_length=250)

    def __str__(self):
        return f'{self.name} - {self.contactNO}'


class Equipment(models.Model):

    name = models.CharField(max_length=120)
    price = models.FloatField(max_length=10)
    unit = models.CharField(max_length=10)
    date = models.DateTimeField(auto_now=True)
    desc = models.TextField(max_length=500)

    def __str__(self):
        return f'{self.name} - {self.unit} - {self.price}'


class Plan(models.Model):

    name = models.CharField(max_length=75)
    desc = models.TextField(max_length=250)
    price = models.FloatField(max_length=7)
    duration = models.FloatField(max_length=5)

    def __str__(self):
        return f'{self.name} - {self.duration} - {self.price}'


class Member(models.Model):

    name = models.CharField(max_length=125)
    contactNo = models.CharField(max_length=10)
    emailId = models.EmailField(max_length=125)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    joinDate = models.DateTimeField(auto_now=True)
    expDate = models.DateTimeField(max_length=20)
    totalAmount = models.FloatField(max_length=10)
    initialAmount = models.FloatField(max_length=10)
    dueAmount = models.FloatField(max_length=10)
    
    def __str__(self):
        return f'{self.name} - {self.plan} - {self.expDate} - {self.dueAmount}'