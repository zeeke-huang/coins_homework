from django.shortcuts import render
from .models import User
from rest_framework import generics
from .serializers import UserSerializer


class UserCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new customer
    queryset = User.objects.all(),
    serializer_class = UserSerializer


class UserList(generics.ListAPIView):
    # API endpoint that allows customer to be viewed.
    queryset = User.objects.all()
    serializer_class = UserSerializer