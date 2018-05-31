from django.db import models

# Create your models here.
from health.models import Counties

class Units(models.Model):
    political_unit_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    subcounty_id = models.IntegerField()
    county_ward = models.IntegerField()



