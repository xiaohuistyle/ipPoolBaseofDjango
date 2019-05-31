# models.py
from django.db import models


class IpModel(models.Model):
    Address = models.CharField(max_length=20)
    port = models.CharField(max_length=20)