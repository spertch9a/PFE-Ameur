from dataclasses import fields
from rest_framework import serializers
from .models import (Patient, Image)


class PatientSerializer(serializers.ModelSerializer):
    class Meta :
        model = Patient
        fields = ('id', 'nom', 'prenom', 'telephon')


class ImageSerializer(serializers.ModelSerializer):
    class Meta :
        model : Image
        fields : '__all__'     

