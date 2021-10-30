from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from .models import Employee


def index(request):
    data = Employee.objects.all()
    context = {'data': data}
    return render(request, 'details.html', context)
