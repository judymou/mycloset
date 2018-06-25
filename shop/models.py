# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import admin

class Item(models.Model):
  image_url = models.CharField(max_length=512)
  title = models.CharField(max_length=500)
  description = models.CharField(max_length=1500)

  def __str__(self):
      return self.title

admin.site.register(Item)
