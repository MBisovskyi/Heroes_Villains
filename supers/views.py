from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SuperSerializer
from .models import Power, Super
from rest_framework import status

# Create your views here.


@api_view(['GET', 'POST'])
def supers_list(request):
    if request.method == 'GET':
        heroes = Super.objects.filter(super_type_id = 1)
        villains = Super.objects.filter(super_type_id = 2)
        supers_param = request.query_params.get('type')
        if supers_param:
            if supers_param == 'hero':
                serializer = SuperSerializer(heroes, many = True)
                return Response(serializer.data)
            elif supers_param == 'villain':
                serializer = SuperSerializer(villains, many = True)
                return Response(serializer.data)
            else:
                answer = 'No Super Type found'
                return Response(answer, status = status.HTTP_204_NO_CONTENT)
        else:
            heroes = heroes_dict(heroes)
            villains = villains_dict(villains)
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
    heroes_list = []
    for hero in heroes:
        hero = {
        "name": hero.name,
        "alter_ego": hero.alter_ego,
        "catchphrase": hero.catchphrase,
        "abilities": get_super_abilities(hero.id),
        }
        heroes_list.append(hero)
    return heroes_list

def villains_dict(villains):
    villains_list = []
    for villain in villains:
        villain = {
        "name": villain.name,
        "alter_ego": villain.alter_ego,
        "catchphrase": villain.catchphrase,
        "abilities": get_super_abilities(villain.id),
        }
        villains_list.append(villain)
    return villains_list

def get_super_abilities(super_id):
    abilities = Power.objects.filter(super = super_id)
    abilities_list = []
    for ability in abilities:
        ability = {
            "id": ability.id,
            "name": ability.name,
        }
        abilities_list.append(ability)
    return abilities_list