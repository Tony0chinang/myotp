from django.db import models

# Create your models here.

class phoneNumber(models.Model):
    mobile = models.IntegerField(blank=False)
    isverified = models.BooleanField(default=False)
    counter = models.IntegerField(default=0, blank= False)
    
    def __str__(self):
        return str(self.mobile)
    
    