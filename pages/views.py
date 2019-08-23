from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from .models import FacultyIteDepartment, FacultyHrmDepartment, SchoolMap, Office

class HomePageView(TemplateView):
    template_name = 'home.html'


class SchoolMapPageView(ListView):
    template_name = 'school_map.html'
    model = SchoolMap


class InformationPageView(TemplateView):
    template_name = 'information.html'


class DepartmentsPageView(TemplateView):
    template_name = 'departments.html'

class OfficeListView(ListView):
    template_name = 'office.html'
    model = Office

class IteDepartmentPageView(ListView):
    model = FacultyIteDepartment
    template_name = 'ite.html'

class FacultyDetailView(DetailView):
    model = FacultyIteDepartment
    template_name = 'faculty_detail.html'

class MapPageView(DetailView):
    model = SchoolMap
    template_name = 'maps.html'

class OfficePageView(DetailView):
    model = Office
    template_name = 'office_detail.html'




