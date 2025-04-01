from rest_framework import serializers
import rest_framework

from .models import Vacancy, Company

class VacancySerializer(serializers.ModelSerializer):
    company = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Vacancy
        fields = ['name', 'description', 'salary', 'company']
        