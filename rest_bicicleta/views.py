from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from bike.models import Bicicleta
from rest_bicicleta.serializers import BicicletaSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def lista_bicicletas(request):
    if request.method == 'GET':
        ListaBicicletas = Bicicleta.objects.all()
        serializer = BicicletaSerializer(ListaBicicletas, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        dataP = JSONParser().parse(request)
        serializer = BicicletaSerializer(data = dataP)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))

def detalle_bicicleta(request, id):
    try:
        bicicleta = Bicicleta.objects.get(idBicicleta=id)
    except Bicicleta.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = BicicletaSerializer(bicicleta)
        return Response(serializer.data)
    elif request.method == "PUT":
        dataP = JSONParser().parse(request)
        serializer = BicicletaSerializer(bicicleta, data = dataP)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        bicicleta.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
# Create your views here.
