from django.db import models
from django.shortcuts import reverse


class Trust(models.Model):
    name = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=200)
    mobile_no = models.CharField(max_length=10)
    email = models.EmailField(unique=True)

    
    def get_absolute_url(self):
        return reverse('food:contact', kwargs={
            'pk':self.pk

        })


    def __str__(self):
        return self.name

   

class PartyHall(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    mobile_no = models.CharField(max_length=10)
    nearby_trust = models.ManyToManyField(Trust)

    def get_absolute_url(self):
        return reverse('food:detail', kwargs={
            'pk':self.pk

        })

    def __str__(self):
        return self.name


