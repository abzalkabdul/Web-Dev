from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status, generics, mixins

from api.serializers import VacancySerializer, CompanySerializer
from api.models import Company, Vacancy


class C_ListAPIView(mixins.ListModelMixin,
                    mixins.CreateModelMixin,

                    generics.GenericAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)
    

class GetCompanyAPIView(APIView):
    def get_object(self, company_id):
        try:
            return Company.objects.get(pk=company_id)
        except Exception as e:
            raise Response({'error': e}, status=status.HTTP_404_NOT_FOUND)
        
    def get(self, request, company_id):
        company = self.get_object(company_id)
        serializer = CompanySerializer(company)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, company_id):
        serializer = CompanySerializer(request.body)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def put(self, request, company_id):
        company = self.get_object(company_id)
        serializer = CompanySerializer(instance=company, data=request.body)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, company_id):
        company = self.get_object(company_id)
        company.delete()
        return Response({"message": f"Company with id-{company_id} is deleted"}, status=status.HTTP_204_NO_CONTENT)


def c_vacancies_list(request, company_id):
        company = Company.objects.get(pk=company_id)
        c_vacancies_list = company.vacancy_set.all()
        serializer = VacancySerializer(c_vacancies_list, many=True)
        return JsonResponse(serializer.data, safe=False, json_dumps_params={'indent': 4})


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
class GetVacancyAPIView(APIView):
    def get_object(self, vacancy_id):
        try:
            return Vacancy.objects.get(pk=vacancy_id)
        except Exception as e:
            raise Response({'error': e}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, vacancy_id):
        vacancy = self.get_object(vacancy_id)
        serializer = VacancySerializer(vacancy)
        return Response(serializer.data)

    def put(self, request, vacancy_id):
        vacancy = self.get_object(vacancy_id)
        serializer = VacancySerializer(instance=vacancy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, vacancy_id):
        vacancy = self.get_object(vacancy_id)
        vacancy.delete()
        return Response({"message": f"Vacancy with id-{vacancy_id} is deleted"})

def list_top_ten(request):
    list_top_ten = Vacancy.objects.order_by("-salary")[:10]
    ten_vacancies = VacancySerializer(list_top_ten, many=True)
    return JsonResponse(ten_vacancies.data, safe=False, json_dumps_params={"indent":4})