from django.http import JsonResponse
from django.shortcuts import render
from .models import Company, Vacancy

def c_list(request):
    c_list = Company.objects.all().values() # Queryset -> ValuesQuerySet(dict)
    return JsonResponse(list(c_list), json_dumps_params = {'indent': 4}) 
