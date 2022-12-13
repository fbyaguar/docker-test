from django.shortcuts import render
from rest_framework import generics, viewsets

from src.customers.models import Profile, Technology
from src.customers.serializers import ProfileSerializer, TechnologySerializer


class ProfileModelViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class TechnologyModelViewSet(viewsets.ModelViewSet):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer
