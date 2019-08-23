from django.urls import path


from .views import (
    HomePageView, 
    SchoolMapPageView, 
    InformationPageView, 
    DepartmentsPageView, 
    OfficePageView, 
    IteDepartmentPageView,
    FacultyDetailView,
    MapPageView,
    OfficeListView,
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('school_map/', SchoolMapPageView.as_view(), name='school_map'),
    path('school_map/<int:pk>/', MapPageView.as_view(), name='maps'),
    path('information/', InformationPageView.as_view(), name='information'),
    path('departments/', DepartmentsPageView.as_view(), name='departments'),
    path('departments/ite/',IteDepartmentPageView.as_view(), name='ite'),
    path('departments/ite/faculty_detail/<int:pk>/', FacultyDetailView.as_view(), name='faculty_detail'),
    path('office/', OfficeListView.as_view(), name='office'),
    path('office/office_detail/<int:pk>', OfficePageView.as_view(), name='office_detail'),
]