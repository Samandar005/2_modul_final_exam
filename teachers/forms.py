from django import forms
from .models import Teacher
import datetime


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = (
            'first_name', 'last_name', 'department', 'subjects',
            'qualification', 'email', 'phone_number', 'address',
            'join_date', 'employment_type', 'image'
        )
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Enter first name',
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Enter last name',
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
            }),
            'department': forms.Select(attrs={
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
            }),
            'subjects': forms.CheckboxSelectMultiple(),
            'qualification': forms.TextInput(attrs={
                'placeholder': 'Enter qualification',
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter email address',
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
            }),
            'phone_number': forms.TextInput(attrs={
                'placeholder': 'Enter phone number',
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
            }),
            'address': forms.Textarea(attrs={
                'placeholder': 'Enter full address',
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
                'rows': 3,
            }),
            'join_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
            }),
            'employment_type': forms.Select(choices=Teacher.EMPLOYMENT_TYPE_CHOICES, attrs={
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
            }),
        }