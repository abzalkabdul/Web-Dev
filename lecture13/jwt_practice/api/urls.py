from django.urls import path, include
from api import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'companies', views.CompanyViewSet, basename='companies')
router.register(r'vacancies', views.VacancyViewSet, basename='vacancies')
urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
]
