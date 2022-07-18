from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SuperSerializer
from .models import Super
from rest_framework import status

# Create your views here.


@api_view(['GET', 'POST'])
def supers_list(request):
    if request.method == 'GET':
        heroes = Super.objects.filter(super_type_id = 1)
        heroes_list = []
        for hero in heroes:
            heroes_list.append(hero)
        villains = Super.objects.filter(super_type_id = 2)
        villains_list = []
        for villain in villains:
                    villains_list.append(villain)
        supers_param = request.query_params.get('type')
        if supers_param:
            if supers_param == 'hero':
                serializer = SuperSerializer(heroes_list, many = True)
                return Response(serializer.data)
            elif supers_param == 'villain':
                serializer = SuperSerializer(villains_list, many = True)
                return Response(serializer.data)
            else:
                answer = 'No Super Type found'
                return Response(answer, status = status.HTTP_204_NO_CONTENT)
        else:
            heroes = heroes_dict(heroes_list)
            villains = villains_dict(villains_list)
            custom_response = {"Heroes": heroes, "Villains": villains}
            return Response(custom_response)            
    elif request.method == 'POST':
        serializer = SuperSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def super_by_id(request, pk):
    super = get_object_or_404(Super, pk = pk)
    if request.method == 'GET':
        super_serializer = SuperSerializer(super)
        return Response(super_serializer.data)
    elif request.method == 'PUT':
        serializer = SuperSerializer(super, data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        super.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

def heroes_dict(heroes):
    heroes_dict = []
    for hero in heroes:
        hero = {
        "name": hero.name,
        "alter_ego": hero.alter_ego,
        "primary_ability": hero.primary_ability,
        "secondary_ability": hero.secondary_ability,
        "catchphrase": hero.catchphrase,
        }
        heroes_dict.append(hero)
    return heroes_dict

def villains_dict(villains):
    villains_dict = []
    for villain in villains:
        villain = {
        "name": villain.name,
        "alter_ego": villain.alter_ego,
        "primary_ability": villain.primary_ability,
        "secondary_ability": villain.secondary_ability,
        "catchphrase": villain.catchphrase,
        }
        villains_dict.append(villain)
    return villains_dict