from django.db import models

# Create your models here.

class Password(models.Model):
    password_text = models.CharField(max_length=200)
class User_ID(models.Model):
    user_id_text = models.CharField(max_length=200)

