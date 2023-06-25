from django.db import models
from django.db import models
from aimals.models import animals

class Lineage(models.Model):
    sno = models.AutoField(primary_key=True)
    animal_id = models.ForeignKey(animals, on_delete=models.CASCADE)
    offspring_names = models.CharField(max_length=255)
    parent_names = models.CharField(max_length=255)

# Create your models here.
