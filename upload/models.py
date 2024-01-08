from django.db import models

# Create your models here.
class StoreUploadImg(models.Model):
    userID = models.IntegerField(primary_key=True)
    image = models.ImageField()