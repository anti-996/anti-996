from django.urls import path

from . import views

urlpatterns = [
    path('', views.company_list, name='index'),
    path('<int:pk>/', views.company_detail, name='detail'),
    path('add/', views.company_add, name='add'),
]
