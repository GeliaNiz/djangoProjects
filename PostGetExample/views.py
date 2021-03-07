from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, viewsets
from rest_framework.decorators import api_view

from .serializers import ExampleSerialize
from .models import Example
from django.http import JsonResponse
from django.forms.models import model_to_dict

@api_view(['GET', 'POST'])
def postGet(request, id=0):
    if request.method == 'POST':
        serializer = ExampleSerialize(data=request.data)
        if serializer.is_valid():
            example = Example(name=serializer.data.get("name"), level=serializer.data.get("level"),
                              degree=serializer.data.get("degree"), place=serializer.data.get("place"),
                              date=serializer.data.get("date")
                              )
            example.save()
            return JsonResponse(ExampleSerialize(example).data, status=status.HTTP_201_CREATED, safe=False)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        if id==0:
            example = Example.objects.all()
            serializer = ExampleSerialize(example, many=True)
        else:
            example = Example.objects.get(id=id)
            serializer = ExampleSerialize(example)
        return JsonResponse(serializer.data, safe=False)
