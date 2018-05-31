from django.db import models

# Create your models here.
from health.models import Counties


class Unit(models.Model):
    administrative_unit_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    subcounty_id = models.IntegerField()
    divisions = models.IntegerField()
    locations = models.IntegerField()
    sub_locations = models.IntegerField()