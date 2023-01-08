from django.db import models

# Create your models here.

class Member(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    location = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    active = models.BooleanField
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class FundRaisingAgent(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    id_number = models.CharField(max_length=30)
    id_proof = models.FileField(upload_to='id_proofs')
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    location= models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    date_joined = models.DateTimeField(auto_now_add=True)
    profile_picture = models.FileField(upload_to='profile_picture')

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class AnnualDonor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class GaleryImage(models.Model):
    image = models.ImageField()


class Message(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.name