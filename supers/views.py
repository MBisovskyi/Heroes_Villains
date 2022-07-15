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
        supers_param = request.query_params.get('type')
        supers = Super.objects.all()
        if supers_param:
            supers = supers.filter(super_type__super_type = supers_param)
        serializer = SuperSerializer(supers, many = True)
        return Response(serializer.data)
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