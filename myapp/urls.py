from django.urls import path, include 
from myapp import views


urlpatterns = [
    
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('test/', views.test_view, name='test_view'),
    path('api/status/', views.api_status, name='api_status'),
]