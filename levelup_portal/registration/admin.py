from django.contrib import admin
from .models import SchoolRegistration, StudentRegistration, PendingStudentRegistration


@admin.register(StudentRegistration)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'studentId', 'full_name', 'email', 'contact', 'school', 'grade', 'created_at')
    search_fields = ('firstName', 'email', 'studentId', 'school__schoolName')
    list_filter = ('grade', 'school')

    def full_name(self, obj):
        return f"{obj.firstName} {obj.middleName} {obj.lastName}"
    full_name.short_description = "Student Name"


@admin.register(SchoolRegistration)
class SchoolAdmin(admin.ModelAdmin):
    list_display = (
        'schoolId',
        'schoolName',
        'schoolEmail',
        'schoolContact',
        'schoolTrust',
        'schoolAffiliation',
        'schoolPrincipalName',
        'schoolPrincipalContact',
        'schoolPrincipalEmail',
        'created_at',
    )
    search_fields = ('schoolName', 'schoolEmail', 'schoolPrincipalName')
    list_filter = ('schoolAffiliation', 'schoolTrust')

@admin.register(PendingStudentRegistration)
class PendingStudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'schoolName', 'schoolAddress', 'schoolPrincipalName', 'schoolPrincipalContact', 'created_at')
    search_fields = ('name', 'email', 'schoolName')
    list_filter = ('created_at',)

    def full_name(self, obj):
        return obj.name
    full_name.short_description = "Student Name"