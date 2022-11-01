from django.db import models


class Request(models.Model):
    message = models.CharField(max_length=10000, null=False)
    source = models.CharField(max_length=128, null=False)
    target = models.CharField(max_length=128, null=False)
