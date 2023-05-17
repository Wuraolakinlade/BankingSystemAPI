from django.shortcuts import render
from django.http import Http404

# Create your views here.

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView


from .models import *
from .serializers import *


class BranchesAPIView(generics.ListCreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

class BranchDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

class BanksAPIView(generics.ListCreateAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

class BankDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
