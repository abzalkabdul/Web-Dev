import json

from api.serializers import VacancySerializer, CompanySerializer
from api.models import Company, Vacancy
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


def c_list(request):
    c_list = Company.objects.all()
    serializer = CompanySerializer(c_list, many=True)
    return Response(serializer.data)


def get_company(request, company_id):
    company = Company.objects.get(pk=company_id)
    serializer = CompanySerializer(company)
    return Response(serializer.data)


def c_vacancies_list(request, company_id):
        company = Company.objects.get(pk=company_id)
        c_vacancies_list = company.vacancy_set.all()
        serializer = VacancySerializer(c_vacancies_list, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def vacancies_list(request):
    if request.method == "GET":
        v_list = Vacancy.objects.all()
        serializer = VacancySerializer(v_list, many=True, read_only=True)
        return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)

    elif request.method == "POST":
        serializer = VacancySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET', 'PUT', 'DELETE'])
def get_vacancy(request, vacancy_id):
    vacancy = Vacancy.objects.get(vacancy_id)

    if request.method == 'GET':
        serializer = VacancySerializer(vacancy)
        return Response(serializer.data)  

    elif request.method == "DELETE":
        vacancy.delete()
        return Response({"message": f"Vacancy with id-{vacancy_id} is deleted"})

    elif request.method == "PUT":
        serializer = VacancySerializer(instance=vacancy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



def list_top_ten(request):
    list_top_ten = Vacancy.objects.order_by("-salary")[:10]
    ten_vacancies = VacancySerializer(list_top_ten, many=True)
    return Response(ten_vacancies.data)