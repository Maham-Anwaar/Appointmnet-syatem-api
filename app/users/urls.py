from django.urls import path, include

from rest_framework.routers import DefaultRouter

from users import views

app_name = 'users'
router = DefaultRouter()
router.register('feed', views.DoctorViewSet)
router.register('users', views.Appointments)


urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.DoctorLoginApiView.as_view(), name='login'),

]
