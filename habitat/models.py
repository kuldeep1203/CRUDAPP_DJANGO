from django.db import models


    


class habitat(models.Model):
    Habitat_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    major_fauna = models.CharField(max_length=255, null=True, blank=True)
    area_covered = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    last_updated=models.DateField(null=True)

    def __str__(self):
        return self.name