import json

from api.serializers import VacancySerializer, CompanySerializer
from api.models import Company, Vacancy
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request


def c_list(Request):
    c_list = Company.objects.all()
    serializer = CompanySerializer(c_list, many=True)
    return Response(serializer.data)


def get_company(Request, company_id):
    company = Company.objects.get(pk=company_id)
    serializer = CompanySerializer(company)
    return Response(serializer.data)


def c_vacancies_list(Request, company_id):
        company = Company.objects.get(pk=company_id)
        c_vacancies_list = company.vacancy_set.all()
        serializer = VacancySerializer(c_vacancies_list, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST', 'PUT'])
def vacancies_list(Request):
    if Request.method == "GET":
        v_list = Vacancy.objects.all()
        serializer = VacancySerializer(v_list, many=True, read_only=True)
        return Response(serializer.data)

    elif Request.method == "POST":
        new_data = json.loads(Request.body)
        serializer = VacancySerializer(data=new_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    elif Request.method == "PUT":
        new_data = json.loads(Request.body)
        vacancy = Vacancy.objects.get(pk=new_data['id'])
        serializer = VacancySerializer(instance=vacancy, data=new_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    


@api_view(['GET', 'DELETE'])
def get_vacancy(Request, vacancy_id):
        
    vacancy = Vacancy.objects.get(pk=vacancy_id)
    serializer = VacancySerializer(vacancy)

    if Request.method == 'GET':
            return Response(serializer.data)  

    elif Request.method=="DELETE":
        vacancy.delete()
        return Response({"message": f"Vacancy with id-{vacancy_id} is deleted"})
    return Response(serializer.data)



def list_top_ten(Request):
    list_top_ten = Vacancy.objects.order_by("-salary")[:10]
    ten_vacancies = VacancySerializer(list_top_ten, many=True)
    return Response(ten_vacancies.data)