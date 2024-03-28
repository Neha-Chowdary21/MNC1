from django.db import models

# Create your models here.
class Neha(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(primary_key=True)
    password=models.CharField(max_length=100)
    phonenumber=models.BigIntegerField()
    class Meta:
        db_table="Neha"

class contactus(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(primary_key=True)
    suggestions=models.CharField(max_length=100)

    class Meta:
        db_table="contactus"





from django.db import models

class Yogi(models.Model):
    username = models.CharField(max_length=100)
    pass1 = models.CharField(max_length=100)
    class Meta:
        db_table = "Yogi"



