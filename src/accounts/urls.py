from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import register_user, user_login, user_logout, change_password, get_user,LaboratoryViewSet,ExperimentViewSet,GroupExperimentViewSet, AnimalViewSet, AnimalDataViewSet

router = DefaultRouter()
router.register(r'laboratory',LaboratoryViewSet, basename='laboratory')
router.register(r'experiment',ExperimentViewSet, basename='experiment')
router.register(r'group_experiment',GroupExperimentViewSet, basename='group_experiment')
router.register(r'animal',AnimalViewSet, basename='animal')
router.register(r'animal_data', AnimalDataViewSet, basename='animal_data')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('register/', register_user, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('change_password/', change_password, name='change_password'),
    path('get_user/', get_user, name='get_user'),
]