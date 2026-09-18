from django.shortcuts import render

# Create your views here.
from app1.models import Employee
from app1.serializaers import EmployeeSerializer
from rest_framework import generics

from app1.models import Employee

class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer