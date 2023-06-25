from django.db import models

from aimals.models import animals

class AMigrations(models.Model):
    migration_id = models.AutoField(primary_key=True)
    animal_id = models.ForeignKey(animals, on_delete=models.CASCADE)
    migration_period = models.CharField(max_length=255)
    migration_from = models.CharField(max_length=255)
    migration_to = models.CharField(max_length=255)
    migration_season = models.CharField(max_length=255)

# Create your models here.
