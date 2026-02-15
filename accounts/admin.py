from django.contrib import admin
from .models import AlumniProfile


@admin.register(AlumniProfile)
class AlumniProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'approved')
    list_editable = ('approved',)



