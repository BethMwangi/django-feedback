from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
LOCATIONS = (  
    ('NRB', 'Nairobi'),
    ('KIS', 'Kisumu'),
    ('MBS', 'Mombasa'),
    ('MACH', 'Machakos'),
    ('KIT', 'Kitui'),)
CHOICES = (('1','1'),
               ('2','2'),
               ('3','3'),
               ('4','4'),)

class Feedback(models.Model):
	username = models.CharField(max_length=200)
	phone_no = models.IntegerField()
	neighbourhood= models.CharField(max_length=20, choices = LOCATIONS)
	rating = models.IntegerField(choices=CHOICES)
	comments = models.CharField(max_length=200)


	def __str__(self):
		return self.username

