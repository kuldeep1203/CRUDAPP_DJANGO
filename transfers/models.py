from django.db import models

# Create your models here.
from django.db import models
from aimals.models import animals

class Transfer(models.Model):
    transfer_id = models.AutoField(primary_key=True)
    animal_id = models.ForeignKey(animals, on_delete=models.CASCADE)
    source = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    reason = models.CharField(max_length=255)
    date_of_transfer = models.DateField()
