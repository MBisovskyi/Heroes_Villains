from django.db import models
from super_types.models import SuperType

# Create your models here.
class Super(models.Model):
    name = models.CharField(max_length = 32)
    alter_ego = models.CharField(max_length = 64)
    primary_ability = models.CharField(max_length = 64)
    secondary_ability = models.CharField(max_length = 64)
    catchphrase = models.CharField(max_length = 128)
    super_type = models.ForeignKey(SuperType, on_delete = models.SET_NULL, null = True)