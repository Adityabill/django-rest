from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
# from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from myapp.models import employees
from .serializers import EmployeeSerializer

@api_view(('GET',))
# @renderer_classes((TemplateHTMLRenderer, JSONRenderer))

# def getData(request):
#     employees = {'name':'Bill', 'location':'Kolkata' }
#     return Response(employees)

# def getEmployees(request):
def getData(request):
    employee_list = employees.objects.all()
    serializer = EmployeeSerializer(employee_list, many = True)
    return Response(serializer.data)

@api_view(['POST'])

def addData(request):
    serializer = EmployeeSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
