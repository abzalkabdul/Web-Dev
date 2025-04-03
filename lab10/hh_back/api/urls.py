from django.urls import path
from api import views

urlpatterns = [
    path('companies/', views.c_list),
    path('companies/<int:company_id>/', views.get_company),
    path('companies/<int:company_id>/vacancies/', views.c_vacancies_list),
    path('vacancies/', views.VacancyListAPIView.as_view()),
    path('vacancies/<int:vacancy_id>/', views.get_vacancy),
    path('vacancies/top_ten/', views.list_top_ten),
]
