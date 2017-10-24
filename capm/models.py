# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm

# Create your models here.
# Create the form class.
class Capm(models.Model):
    risk_free_rate = models.IntegerField()
    beta = models.IntegerField()
    market_return = models.IntegerField()


    def __str__(self):              # __unicode__ on Python 2
        return self.id

