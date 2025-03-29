from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.shortcuts import render
from .models import Company, Vacancy

def c_list(request):
    c_list = Company.objects.all().values() # Queryset -> ValuesQuerySet(dict)
    return JsonResponse(list(c_list), safe=False, json_dumps_params = {'indent': 4})

def get_company(request, company_id):
    try:
        company = Company.objects.get(pk=company_id)
        company_data = model_to_dict(company)
    except Company.DoesNotExist as e:
        return JsonResponse({"error": str(e)}, status=404)

    return JsonResponse(company_data, json_dumps_params={'indent': 4})

def c_vacancies_list(request, company_id):
    try: 
        company = Company.objects.get(pk=company_id)
        c_vacancies_list = company.vacancy_set.all().values()
    except Company.DoesNotExist as e:
        return JsonResponse({"error": str(e)}, status=404)

    return JsonResponse(list(c_vacancies_list), safe=False, json_dumps_params={"indent": 4})

def vacancies_list(request):
    v_list = Vacancy.objects.all().values()
    return JsonResponse(list(v_list), safe=False, json_dumps_params={'indent': 4})

def get_vacancy(request, vacancy_id):
    try: 
        vacancy = Vacancy.objects.get(pk=vacancy_id)
        vacancy_data = model_to_dict(vacancy)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({"error": str(e)}, json_dumps_params={"indent": 4}) 

    return JsonResponse(vacancy_data, json_dumps_params={"indent": 4})

def list_top_ten(request):
    top_ten = Vacancy.objects.order_by("-salary")[:10]
    list_top_ten = [model_to_dict(t) for t in top_ten]
    return JsonResponse(list_top_ten, safe=False, json_dumps_params={"indent":4})