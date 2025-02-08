from django.contrib import admin
from .models import Teacher

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'position', 'status', 'employment_type', 'department', 'author')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('status', 'employment_type', 'department')
    filter_horizontal = ('subjects',)
