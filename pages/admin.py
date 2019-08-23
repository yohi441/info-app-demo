from django.contrib import admin


from .models import FacultyIteDepartment, FacultyHrmDepartment, SchoolMap, Office, FrequentlyAskedQuestion

admin.site.site_header = 'Cdk Information Kiosk Administration'
admin.site.register(FacultyIteDepartment)
admin.site.register(FacultyHrmDepartment)
admin.site.register(SchoolMap)
admin.site.register(Office)
admin.site.register(FrequentlyAskedQuestion)


