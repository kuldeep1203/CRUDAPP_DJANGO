from django.db import models
from habitat.models import habitat
from datetime import date
class animals(models.Model):
    animal_id=models.BigIntegerField(primary_key=True)
    aname=models.CharField(max_length=40)
    sex=models.CharField(max_length=10)
    dob=models.DateField()
  
    age=models.IntegerField()
    specices=models.CharField(max_length=256)
    date_of_death=models.DateField(null=True,blank=True)
    date_of_arrival=models.DateField()
    description=models.CharField(max_length=255,null=True,blank=True)
    Habitat_id=models.ForeignKey(habitat,on_delete=models.SET_NULL, null=True,db_column='Habitat_id')
    last_updated=models.DateField(null=True)

    def __str__(self):
        return self.aname
    
    """
    def age(self):
        today = date.today()
        age = today.year - self.dob.year
        # Check if the birthday has already occurred this year
        if today < date(today.year, self.dob.month, self.dob.day):
            age -= 1
        return age 
    
    def save(self, *args, **kwargs):
        self.age = self.age()  # Calculate the age based on the dob field
        super().save(*args, **kwargs)"""