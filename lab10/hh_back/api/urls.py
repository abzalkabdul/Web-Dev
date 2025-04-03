from django.urls import path
from api import views

urlpatterns = [
    path('companies/', views.c_list),
    path('companies/<int:company_id>/', views.GetCompanyAPIView.as_view()),
    path('companies/<int:company_id>/vacancies/', views.c_vacancies_list),
    path('vacancies/', views.vacancies_list),
    path('vacancies/<int:vacancy_id>/', views.GetVacancyAPIView.as_view()),
    path('vacancies/top_ten/', views.list_top_ten),
]
