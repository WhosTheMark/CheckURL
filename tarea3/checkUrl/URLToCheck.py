from django.db import models

class URLToCheck(models.Model):
   direccion = models.CharField(max_length = 200)