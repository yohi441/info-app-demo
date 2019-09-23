from django.urls import path


from .views import (
    HomePageView, 
    SchoolMapPageView, 
    InformationPageView, 
    DepartmentsListView, 
    OfficeDetailView,
    OfficePageListView, 
    FacultyDetailView,
    MapPageView,
    OfficeListView,
    InformationDetailView,
    FacultyListView,
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('school-map/', SchoolMapPageView.as_view(), name='school_map'),
    path('school-map/<int:pk>/', MapPageView.as_view(), name='maps'),
    path('information/', InformationPageView.as_view(), name='information'),
    path('information/information-detail/<int:pk>/', InformationDetailView.as_view(), name='information_detail'),
    path('departments/', DepartmentsListView.as_view(), name='departments'),
    path('departments/faculty-list/<int:pk>', FacultyListView.as_view(), name='department_list'),
    path('departments/faculty-detail/<int:pk>/', FacultyDetailView.as_view(), name='faculty_detail'),
    path('office/', OfficeListView.as_view(), name='office'),
    path('office/list/<int:pk>', OfficePageListView.as_view(), name='office_list'),
    path('office/detail/<int:pk>/', OfficeDetailView.as_view(), name='office_detail'),
]