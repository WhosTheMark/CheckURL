from django.db import models

class urlToCheck(models.Model):
   direccion = models.CharField(max_length = 200)