from django.contrib import admin

from candidateProfile.models import personal_details,Education,Experience,Skills,Projects,keyAchievements,Languages

# Register your models here.
admin.site.register(personal_details)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Skills)
admin.site.register(keyAchievements)
admin.site.register(Projects)
admin.site.register(Languages)


