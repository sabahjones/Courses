# Inside models.py
from __future__ import unicode_literals

from django.db import models


class Catalog(models.Model):
  course_name = models.CharField(max_length=100)
  description = models.TextField(max_length=500)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
