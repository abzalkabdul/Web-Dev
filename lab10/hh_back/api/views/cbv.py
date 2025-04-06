from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status, generics, mixins

from api.serializers import VacancySerializer, CompanySerializer
from api.models import Company, Vacancy


class C_ListAPIView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    

class GetCompanyAPIView(generics.RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    lookup_url_kwarg = 'company_id'


class C_VacanciesListAPIView(generics.ListCreateAPIView):
    serializer_class = VacancySerializer

    def get_queryset(self):     #just magic
        company_id = self.kwargs.get('company_id')
        try:
            company = Company.objects.get(pk=company_id)
        except Exception as e:
            raise Response({'error': 'idiot'}, status=status.HTTP_404_NOT_FOUND)
        return company.vacancy_set.all()


class VacanciesListAPIView(generics.ListCreateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    
class GetVacancyAPIView(generics.RetrieveUpdateDestroyAPIView):  
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    lookup_url_kwarg='vacancy_id'

class ListTopTenAPIView(generics.ListAPIView): 
    queryset = Vacancy.objects.order_by("-salary")[:10]
    serializer_class = VacancySerializer
