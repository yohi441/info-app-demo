from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, View
from django.db import connection

from .models import (
    Faculty, 
    SchoolMap, 
    Office,
    Department,
    FrequentlyAskedQuestion,
    StaffMember
)

class HomePageView(TemplateView):
    template_name = 'home.html'


class SchoolMapPageView(ListView):
    template_name = 'school_map.html'
    model = SchoolMap


class InformationPageView(ListView):
    model = FrequentlyAskedQuestion
    template_name = 'information.html'


class DepartmentsListView(ListView):
    model = Department
    template_name = 'departments.html'

class OfficeListView(ListView):
    model = Office
    template_name  = 'office.html'

class FacultyDetailView(DetailView):
    model = Faculty
    template_name = 'faculty_detail.html'

    """ def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        context = super(FacultyDetailView, self).get_context_data(**kwargs)
        context['department'] = Department.objects.get(id=pk)
        return context """


class MapPageView(DetailView):
    model = SchoolMap
    template_name = 'maps.html'

class OfficeDetailView(DetailView):
    model = StaffMember
    template_name = 'office_detail.html'

class InformationDetailView(DetailView):
    model = FrequentlyAskedQuestion
    template_name = 'information_detail.html'

class FacultyListView(ListView):
    model = Faculty
    template_name = 'faculty_list.html'
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Faculty.objects.filter(department__id=pk)

    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        context = super(FacultyListView, self).get_context_data(**kwargs)
        context['department'] = Department.objects.get(id=pk)
        return context

class OfficePageListView(ListView):
    model = StaffMember
    template_name = 'office_list.html'

    def get_queryset(self):
        pk = self.kwargs['pk']
        return StaffMember.objects.filter(office__id=pk)

    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        context = super(OfficePageListView, self).get_context_data(**kwargs)
        context['office'] = Office.objects.get(id=pk)
        return context



