from django.contrib import admin
from .models import Subject

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'grade_level', 'credit_hours', 'status', 'department', 'author')
    search_fields = ('name',)
    list_filter = ('status', 'grade_level')
