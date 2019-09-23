from django.contrib import admin


from .models import (
    Faculty, 
    SchoolMap, 
    Office, 
    FrequentlyAskedQuestion,
    Department,
    StaffMember,
)
 
class DepartmentFacultyList(admin.ModelAdmin):
    model = Faculty
    list_display = ('lastname','middle_initial','name','department',)

    def get_name(self, obj):
        return obj.department.name
    get_name.admin_order_field = 'department'
    get_name.short_description = 'Department Name'



class StaffMemberList(admin.ModelAdmin):
    model = StaffMember
    list_display = ('lastname', 'name', 'office')

    def get_name(self, obj):
        return obj.office.name
    
    get_name.admin_order_field = 'office'
    get_name.short_description = 'Office name'
    

admin.site.site_header = 'Cdk Information Kiosk Administration'
admin.site.register(SchoolMap)
admin.site.register(Office)
admin.site.register(FrequentlyAskedQuestion)
admin.site.register(Faculty, DepartmentFacultyList)
admin.site.register(Department,)
admin.site.register(StaffMember, StaffMemberList)



