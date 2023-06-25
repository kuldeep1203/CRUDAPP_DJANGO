from django.db import models
from aimals.models import animals
# Create your models here.

class Health(models.Model):
    report_id_number = models.AutoField(primary_key=True)
    animal_id = models.ForeignKey(animals, on_delete=models.CASCADE)
    health_condition = models.CharField(max_length=255)
    treatment = models.CharField(max_length=255)
    past_treatments = models.TextField()
    past_diseases = models.TextField()

    
