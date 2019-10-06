from django.db import models

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    mobile = models.BigIntegerField()
    sex = models.CharField(max_length=6)
    address = models.CharField(max_length=255)
    occupation = models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = 'patient'
