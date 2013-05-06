from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=50)
    store = models.ForeignKey('Store')

    def __unicode__(self):
        return self.name
