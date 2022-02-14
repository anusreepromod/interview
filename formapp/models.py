from django.db import models

# Create your models here.


class register(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    mobile = models.CharField(max_length=40)


class login(models.Model):
    username = models.EmailField()
    password = models.CharField(max_length=20)
    user_id = models.ForeignKey(register, on_delete=models.CASCADE)
