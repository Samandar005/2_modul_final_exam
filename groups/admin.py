from django.contrib import admin
from .models import Group

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'academic_year', 'grade_level', 'schedule', 'max_students', 'status', 'teacher', 'author')
    search_fields = ('name', 'academic_year')
    list_filter = ('status', 'grade_level', 'schedule')
    filter_horizontal = ('subjects',)
