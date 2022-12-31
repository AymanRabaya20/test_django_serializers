from rest_framework import viewsets
from rest_framework.decorators import action
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.response import Response


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    @action(detail=True, methods=['GET'])
    def info(self, request, pk=None):
        queryset = Employee.objects.filter(pk=pk)
        sr = EmployeeSerializer(queryset, many=True)
        return Response({'data': sr.data})

