from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .serializers import RoomSerializer
from .models import Room

# Create your views here. the after the / on the website

# def hello(request):
#     return HttpResponse('<h1> sup my mello </h1>')

class RoomView(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


