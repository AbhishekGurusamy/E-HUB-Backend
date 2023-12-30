from django.db import models

# Create your models here.
class StoreUploadImg(models.Model):
    userID = models.IntegerField(max_length = 20)
    imgURL = models.CharField()