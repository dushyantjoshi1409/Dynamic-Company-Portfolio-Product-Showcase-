from django.urls import path
from . import views

urlpatterns = [
    path('', views.Allcompany.as_view(), name = 'allcompany'),
    path('<int:pk>/', views.CompanyDetails.as_view(), name = 'detail'),
    path('create/', views.AddCompany.as_view(), name='addcomapny'),
    path('update/<int:pk>/', views.EditCompany.as_view(), name='update'),
]