from django.db import models

# Create your models here.

class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    mobile = models.BigIntegerField()
    sex = models.CharField(max_length=6)
    address = models.CharField(max_length=255)
    occupation = models.CharField(max_length=20)

    contineous = models.CharField(max_length=50, blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    aggravating = models.CharField(max_length=50, blank=True, null=True)
    relieving = models.CharField(max_length=50, blank=True, null=True)
    duration = models.CharField(max_length=50, blank=True, null=True)

    disease = models.CharField(max_length=20, blank=True, null=True)
    recent_wt_loss = models.IntegerField(blank=True, null=True)
    breathing_pattern = models.CharField(max_length=20, blank=True, null=True)
    heal_walking = models.CharField(max_length=20, blank=True, null=True)
    
    morning_stiffness = models.CharField(max_length=50, blank=True, null=True)
    numbness = models.CharField(max_length=50, blank=True, null=True)
    mechanical_injury = models.CharField(max_length=50, blank=True, null=True)
    mascular_weakness = models.CharField(max_length=50, blank=True, null=True)
    sleeping_disturbance = models.CharField(max_length=50, blank=True, null=True)
    mode_of_onset = models.CharField(max_length=50, blank=True, null=True)
    claudication = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient'