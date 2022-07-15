from django.db import models

# Create your models here.
class SuperType(models.Model):
    super_type = models.CharField(max_length = 32)