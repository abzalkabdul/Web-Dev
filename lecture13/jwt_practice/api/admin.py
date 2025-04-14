from django.contrib import admin
from api.models import Company, Vacancy

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']
    search_fields = ('name', 'description')

@admin.register(Vacancy)
class Vacancy(admin.ModelAdmin):
    list_display = ['id','salary', 'company']
    search_fields = ('salary', 'company')