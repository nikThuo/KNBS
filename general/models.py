from django.db import models

# Create your models here.
class Request_Dataset(models.Model):
    request_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=70)
    dataset = models.CharField(max_length=100)
    year = models.IntegerField()
