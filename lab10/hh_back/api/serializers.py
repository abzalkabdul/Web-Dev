from rest_framework import serializers
import rest_framework

from .models import Vacancy, Company

'''
# Using just Serializer

class VacancySerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()
    salary = serializers.FloatField()
    company = serializers.PrimaryKeyRelatedField(queryset=Vacancy.objects.all())
'''

# Using serializer class
class VacancySerializer(serializers.ModelSerializer):
    company = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all())

    class Meta:
        model = Vacancy
        fields = '__all__'
        
'''
class CompanySerializer(serializer.Serializer):
    name = serializer.CharField()
    description = serializer.CharField()
    city = serializer.CharField()
    address = serializer.CharField()
'''
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
