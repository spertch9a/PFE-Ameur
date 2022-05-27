import json
from django.shortcuts import render
from .serializer import (PatientSerializer, ImageSerializer)
from .models import (Image, Patient)
from django.http import JsonResponse
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class PatientList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        print(' DATA ', serializer.data)
        # return Response(serializer.data, status = status.HTTP_200_OK)
        return JsonResponse({'Patient' : serializer.data}, safe = False , status = status.HTTP_200_OK)

        

    def post(self, request, format=None):
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ImagesList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        patients = Image.objects.all()
        serializer = ImageSerializer(patients, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
        

    def post(self, request, format=None):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)