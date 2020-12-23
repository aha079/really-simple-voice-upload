from django.db import models

class Voice(models.Model):
    docfile = models.FileField(upload_to='voice/%Y/%m/%d')