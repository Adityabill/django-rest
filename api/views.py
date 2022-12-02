from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])

def getData(request):
    employees = {'name':'Bill', 'location':'Kolkata' }
    return Response(employees)