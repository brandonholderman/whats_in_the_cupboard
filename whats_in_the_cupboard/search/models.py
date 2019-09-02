# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from PIL import Image


# Create your models here.
class Search(models.Model):
    label = models.CharField(max_length=200, blank=True, null=True)
    favorites = models.FileField(upload_to='favorites/')
    image_url = models.ImageField(
        default=timezone.now, upload_to='recipe_img/')
    directions_url = models.URLField(max_length=200, blank=True, null=True)
    ingredients = models.TextField(max_length=None, blank=True, null=True)
    calories = models.FloatField(blank=True, max_length=100, null=True)
    total_time = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.label
