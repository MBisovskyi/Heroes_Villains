from django.db import models
from super_types.models import SuperType

# Create your models here.
class Super(models.Model):
    name = models.CharField(max_length = 32)
    alter_ego = models.CharField(max_length = 64)
    powers = models.ManyToManyField('Power')
    catchphrase = models.CharField(max_length = 128)
    super_type = models.ForeignKey(SuperType, on_delete = models.SET_NULL, null = True)
    def __str__(self):
        return self.name

class Power(models.Model):
    name = models.CharField(max_length = 64)
    def __str__(self):
        return self.name