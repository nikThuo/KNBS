from django.db import models

# Create your models here.
class Per_Change_In_Quantum_Indices_Of_Man_Production(models.Model):
    percentage_change_id = models.AutoField(primary_key=True)
    commodity = models.CharField(max_length=200)
    percentage_change = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.IntegerField()

class Quantum_Indices_Of_Manufacturing_Production(models.Model):
    quantum_indice_id = models.AutoField(primary_key=True)
    commodity = models.CharField(max_length=200)
    quantum_indice = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.IntegerField()