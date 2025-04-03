import json

from api.serializers import VacancySerializer, CompanySerializer
from api.models import Company, Vacancy
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
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


@api_view(['GET', 'POST'])
def vacancies_list(Request):
    if Request.method == "GET":
        v_list = Vacancy.objects.all()
        serializer = VacancySerializer(v_list, many=True, read_only=True)
        return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)

    elif Request.method == "POST":
        serializer = VacancySerializer(data=Request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET', 'PUT', 'DELETE'])
def get_vacancy(Request, vacancy_id):
    vacancy = Vacancy.objects.get(vacancy_id)

    if Request.method == 'GET':
        serializer = VacancySerializer(vacancy)
        return Response(serializer.data)  

    elif Request.method == "DELETE":
        vacancy.delete()
        return Response({"message": f"Vacancy with id-{vacancy_id} is deleted"})

    elif Request.method == "PUT":
        serializer = VacancySerializer(instance=vacancy, data=Request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



def list_top_ten(Request):
    list_top_ten = Vacancy.objects.order_by("-salary")[:10]
    ten_vacancies = VacancySerializer(list_top_ten, many=True)
    return Response(ten_vacancies.data)