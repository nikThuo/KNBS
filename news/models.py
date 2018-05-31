from django.db import models

# Create your models here.
class Updates(models.Model):
    news_id = models.AutoField(primary_key=True)
    title = models.CharField(default=True, max_length=100)
    news = models.CharField(max_length=2000)
    source = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
