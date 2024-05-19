from django.db import models

# Create your models here.
class Member(models.Model):
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)
    confirm_password=models.CharField(max_length=100)


class user(models.Model):
    title=models.CharField(max_length=300)
    story=models.CharField(max_length=3000)

class log(models.Model):
    emails=models.EmailField(max_length=100)
    passwords=models.CharField(max_length=20)

class message(models.Model):
    email=models.EmailField(max_length=100)
    message=models.CharField(max_length=1000)
