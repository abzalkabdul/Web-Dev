from argparse import Action
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from rest_framework import status, generics, mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny


from api.serializers import VacancySerializer, CompanySerializer
from api.models import Company, Vacancy

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    
    def get_permissions(self):
        if self.action == 'list':
            return [IsAuthenticated()]
        return [AllowAny()]
    
    @action(detail=True, methods=['get', 'post'])
    def vacancies(self, request):
        try:
            company = self.get_object()
        except Company.DoesNotExist:
            raise Response({'error': 'Company not found'},
                           status=status.HTTP_404_NOT_FOUND)

        if request.method == "GET":
            vacancies = Vacancy.objects.filter(company=company)
            serializer = VacancySerializer(vacancies, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif request.method == "POST":
            new_vacancy = VacancySerializer(data=request.body)
            if new_vacancy.is_valid():
                new_vacancy.save()
                return Response(new_vacancy.data, status=status.HTTP_201_CREATED)
            return Response(new_vacancy.errors, status=status.HTTP_400_BAD_REQUEST)
    


class VacancyViewSet(viewsets.ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer

        
    @action(detail=False, methods=['get'])
    def top_ten(self, request, *args, **kwargs):
        top_ten = Vacancy.objects.order_by('-salary')[:10]
        serializer = VacancySerializer(top_ten, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
