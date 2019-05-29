# models.py
from django.db import models


class IpModel(models.Model):
    name = models.CharField(max_length=20)