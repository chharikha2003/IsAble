from django.contrib import admin

from candidateProfile.models import personal_details,Education,Experience,Skills,Certifications,Projects

# Register your models here.
admin.site.register(personal_details)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Skills)
admin.site.register(Certifications)
admin.site.register(Projects)


