from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    # path('employees', views.getEmployees),
    path('add', views.addData),
]