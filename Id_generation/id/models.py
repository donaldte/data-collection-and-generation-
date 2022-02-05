import datetime
from django.db import models
from django.contrib.auth.models import User 
from random import randint


# Create your models here.

#This will be your table where you'll save the information

class UserProfile(models.Model):
    identification = models.CharField(unique=True, max_length=1000)
    name = models.CharField(max_length=1000)
    username = models.CharField(max_length=1000)
    date = models.DateField()
    place = models.CharField(max_length=1000)
    email = models.EmailField()
    pwd = models.CharField(max_length=1000)
    status = models.CharField(max_length=1000)
    sex = models.CharField(max_length=1000)
    matrial = models.CharField(max_length=1000)
    activite = models.CharField(max_length=1000)
    NomDeLaMere = models.CharField(max_length=1000)
    PrenomDeLaMere = models.CharField(max_length=1000)
    NomDuLaPere = models.CharField(max_length=1000)
    PrenomDuLaPere = models.CharField(max_length=1000)
    pays = models.CharField(max_length=1000)
    ville = models.CharField(max_length=1000)
    ndd = models.CharField(max_length=1000)
    ddlIDCOMMUNE2 = models.CharField(max_length=1000)
    txtCOMMUNE2 = models.CharField(max_length=1000)
    quatier = models.CharField(max_length=1000)
    Lieu_dit = models.CharField(max_length=1000)
    Unite_de_gestion = models.CharField(max_length=1000)
    tel = models.CharField(max_length=1000)
    date_added = models.DateTimeField(auto_now_add=True)

    class meta: 
        ordering = ['-date_added']
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """
        This function help you tho get the identification you can modifiy if the structure isn't good
        """
        dt = datetime.datetime.now().year
        
        count = randint(100, 999)
        first = self.name[0].upper()
        second = self.username[0].upper()
        third = self.pays[0].upper()
        self.identification = str( first + "100"+ second + third+ str(dt) + str(self.date)[4] + "-0"+ str(count) )
         
        return super().save(*args, **kwargs)


        




# make with heart by Donald