from django.contrib import admin
from .models import AlumniProfile, Skill


class AlumniProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'approved')
    list_editable = ('approved',)


admin.site.register(AlumniProfile, AlumniProfileAdmin)
admin.site.register(Skill)





