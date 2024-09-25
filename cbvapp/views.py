from django.shortcuts import render, HttpResponse
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView
from .models import Company 

class Myclass(TemplateView):
    template_name = "index.html"
    # def get(self, request):
    #     return HttpResponse("hiii")
    
class Allcompany(ListView):
    model = Company
    context_object_name = "allcompanies"

class CompanyDetails(DetailView):
    model = Company
    context_object_name = "company_details"

class AddCompany(CreateView):
    model = Company
    fields = "__all__"