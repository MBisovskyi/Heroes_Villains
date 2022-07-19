from rest_framework import serializers
from .models import Power, Super

class SuperSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Super
        fields = ['name', 'alter_ego', 'catchphrase', 'powers', 'super_type', 'super_type_id']
        depth = 1

    super_type_id = serializers.IntegerField(write_only = True)