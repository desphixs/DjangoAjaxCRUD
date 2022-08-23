from atexit import register
from django.contrib import admin
from base.models import Student
from import_export.admin import ImportExportModelAdmin

class StudentAdmin(ImportExportModelAdmin):
    pass

admin.site.register(Student, StudentAdmin)