from django.shortcuts import render
from .models import GSM
from .serializers import GSMSerializer
from rest_framework import viewsets
from rest_framework.response import Response

from django.http import HttpResponse
# Create your views here.
def Hello(request):
    return HttpResponse("HELLO WORLD")


class GSMViewSet(viewsets.ModelViewSet):
    queryset = GSM.objects.all()
    serializer_class = GSMSerializer

