from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create-admin/', views.create_admin, name='create_admin')
]