import json
from django.http import JsonResponse
from rest_framework.views import APIView

from api.serializers import VacancySerializer, CompanySerializer
from api.models import Company, Vacancy
from django.views.decorators.csrf import csrf_exempt

class VacancyListAPIView(APIView):

    def get(self, request):
        v_list = Vacancy.objects.all()
        serializer = VacancySerializer(v_list, many=True, read_only=True)
        return JsonResponse(serializer.data, safe=False, json_dumps_params={'indent': 4})
    
    def post(self, request):
        new_data = json.loads(request.body)
        serializer = VacancySerializer(data=new_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    


def c_list(request):
    c_list = Company.objects.all()
    serializer = CompanySerializer(c_list, many=True)
    return JsonResponse(serializer.data, safe=False, json_dumps_params = {'indent': 4})


def get_company(request, company_id):
    company = Company.objects.get(pk=company_id)
    serializer = CompanySerializer(company)
    return JsonResponse(serializer.data, json_dumps_params={"indent": 4})


def c_vacancies_list(request, company_id):
        company = Company.objects.get(pk=company_id)
        c_vacancies_list = company.vacancy_set.all()
        serializer = VacancySerializer(c_vacancies_list, many=True)
        return JsonResponse(serializer.data, safe=False, json_dumps_params={'indent': 4})


@csrf_exempt
def vacancies_list(request):
    if request.method == "GET":
        v_list = Vacancy.objects.all()
        serializer = VacancySerializer(v_list, many=True, read_only=True)
        return JsonResponse(serializer.data, safe=False, json_dumps_params={'indent': 4})

    elif request.method == "POST":
        new_data = json.loads(request.body)
        serializer = VacancySerializer(data=new_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "PUT":
        new_data = json.loads(request.body)
        vacancy = Vacancy.objects.get(pk=new_data['id'])
        serializer = VacancySerializer(instance=vacancy, data=new_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)
    


@csrf_exempt
def get_vacancy(request, vacancy_id):
    try: 
        vacancy = Vacancy.objects.get(pk=vacancy_id)
        vacancy_data = VacancySerializer(vacancy)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({"error": str(e)}, status=400) 
    
    if request.method=="DELETE":
        vacancy.delete()
        return JsonResponse({"message": f"Vacancy with id-{vacancy_id} is deleted"})
    return JsonResponse(vacancy_data, json_dumps_params={"indent": 4})



def list_top_ten(request):
    list_top_ten = Vacancy.objects.order_by("-salary")[:10]
    ten_vacancies = VacancySerializer(list_top_ten, many=True)
    return JsonResponse(ten_vacancies.data, safe=False, json_dumps_params={"indent":4})