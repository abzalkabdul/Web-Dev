import json
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.shortcuts import render
from .models import Company, Vacancy
from django.views.decorators.csrf import csrf_exempt


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


@csrf_exempt
def vacancies_list(request):
    if request.method == "GET":
        v_list = Vacancy.objects.all()
        v_list_json = [v.to_json() for v in v_list]
        return JsonResponse(v_list_json, safe=False, json_dumps_params={'indent': 4})
    
    elif request.method=="POST":
        data = json.loads(request.body)
        # ForeignKey expects a Company object, not just an ID.
        company = Company.objects.get(id=data['company_id'])
        try:
            vacancy = Vacancy.objects.create(
                name=data['name'],
                description=data['description'],
                salary=data['salary'],
                company=company,
            )
        except Exception as e:
            return JsonResponse({'error': str(e)})
        
        return JsonResponse(vacancy.to_json(), status=201)
    
    # If ID is included in the JSON request, we should use PUT or DELETE instead of POST.
    elif request.method == "PUT": 
        data = json.loads(request.body)
        # ForeignKey expects a Company object, not just an ID.
        company = Company.objects.get(id=data['company_id'])
        try:
            vacancy = Vacancy.objects.get(id=data['id'])
            vacancy.name=data['name']
            vacancy.description=data['description']
            vacancy.salary=data['salary']
            vacancy.company=company
            vacancy.save()
            return JsonResponse(vacancy.to_json())
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=404)

        


@csrf_exempt
def get_vacancy(request, vacancy_id):
    try: 
        vacancy = Vacancy.objects.get(pk=vacancy_id)
        vacancy_data = model_to_dict(vacancy)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({"error": str(e)}, json_dumps_params={"indent": 4}) 
    
    if request.method=="DELETE":
        vacancy.delete()
        return JsonResponse({"message": f"Vacancy with id-{vacancy_id} is deleted"})

    return JsonResponse(vacancy_data, json_dumps_params={"indent": 4})

def list_top_ten(request):
    top_ten = Vacancy.objects.order_by("-salary")[:10]
    list_top_ten = [model_to_dict(t) for t in top_ten]
    return JsonResponse(list_top_ten, safe=False, json_dumps_params={"indent":4})