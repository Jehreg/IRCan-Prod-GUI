from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    key = models.CharField(max_length=4096)

class Client(models.Model):
    name = models.CharField(max_length=128)
    contact_name = models.CharField(max_length=30,blank=True)
    contact_email = models.CharField(max_length=128,blank=True)

    user = models.ManyToManyField(User, through='Membership')

    def __unicode__(self):
        return self.name

class Membership(models.Model):
    user = models.ForeignKey(User)
    client = models.ForeignKey(Client)

    is_admin = models.BooleanField()
