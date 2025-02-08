from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'status', 'grade', 'group', 'author')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('status', 'grade', 'gender', 'group')
