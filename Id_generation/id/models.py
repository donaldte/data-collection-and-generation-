import datetime
from django.db import models


# Create your models here.

#This will be your table where you'll save the information

class UserProfile(models.Model):
    identification = models.CharField(unique=True, primary_key=True, max_length=1000)
    first_name  = models.CharField(max_length=200)
    last_name  = models.CharField(max_length=200)
    Born_year = models.DateField()
    
    def __str__(self):
        return self.first_name

    def save(self, *args, **kwargs):
        """
        This function help you tho get the identification you can modifiy if the structure isn't good
        """
        dt = datetime.datetime.now().year

        count = 0
        self.identification = str( self.first_name[0] + "100"+ str(dt) + str(self.Born_year)[4] + "-0"+ str(count) )
        count +=1  
        return super().save(*args, **kwargs)




# make with heart by Donald