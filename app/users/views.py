from typing import Generic
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.authtoken.models import Token
from users import models
from users import serializers


class DoctorViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.DoctorSerializer
    queryset = models.Doctor.objects.all()


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })


class DoctorLoginApiView(CustomAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class Appointments(viewsets.ModelViewSet):
    serializer_class = serializers.AppointmnetDetailsSerializer
    queryset = models.Appointment.objects.filter(d_id='4')



class Appointments(viewsets.ModelViewSet):
    serializer_class = serializers.AppointmnetDetailsSerializer
    queryset = models.Appointment.objects.filter(d_id='4')
