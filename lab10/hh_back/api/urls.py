from django.urls import path
from api import views

urlpatterns = [
    path('companies/', views.C_ListAPIView.as_view()),
    path('companies/<int:company_id>/', views.GetCompanyAPIView.as_view()),
    path('companies/<int:company_id>/vacancies/', views.C_VacanciesListAPIView.as_view()),
    path('vacancies/', views.VacanciesListAPIView.as_view()),
    path('vacancies/<int:vacancy_id>/', views.GetVacancyAPIView.as_view()),
    path('vacancies/top_ten/', views.ListTopTenAPIView.as_view()),
]
