import datetime
from django.db import models
from django.contrib.auth.models import User 
from random import randint


# Create your models here.

#This will be your table where you'll save the information

class UserProfile(models.Model):
    identification = models.CharField(unique=True, max_length=1000)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Born_year = models.DateField() # format 2222-06-01
    date = models.DateTimeField(auto_now=True)

    class meta: 
        ordering = ['-date']
    
    def __str__(self):
        return self.user.first_name

    def save(self, *args, **kwargs):
        """
        This function help you tho get the identification you can modifiy if the structure isn't good
        """
        dt = datetime.datetime.now().year
        
        count = randint(100, 500)
        first = self.user.first_name[0].upper()
        self.identification = str( first + "100"+ str(dt) + str(self.Born_year)[4] + "-0"+ str(count) )
         
        return super().save(*args, **kwargs)


        




# make with heart by Donald