from rest_framework.response import Response
from rest_framework.decorators import api_view
from myapp.models import employees
from .serializers import EmployeeSerializer

@api_view(('GET',))

# def getData(request):
#     employees = {'name':'Bill', 'location':'Kolkata' }
#     return Response(employees)

#def getEmployees(request):
def getData(request):
    employee_list = employees.objects.all()
    serializer = EmployeeSerializer(employee_list, many = True)
    return Response(serializer.data)