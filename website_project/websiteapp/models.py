from django.db import models

# Create your models here.
class Links(models.Model):

    def __str__(self):
        return self.strname
    address=models.CharField(max_length=500,null=True,blank=True)
    strname=models.CharField(max_length=500,null=True,blank=True)