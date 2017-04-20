from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=6)
    password = models.CharField(max_length=12)

    def __unicode__(self):
        return u'%s %s' % (self.name,self.password)
