from django import forms
from .models import Group
from teachers.models import Teacher

class GroupForm(forms.ModelForm):
    teachers = forms.ModelMultipleChoiceField(
        queryset=Teacher.objects.all(),
        widget=forms.SelectMultiple(attrs={
            'class': 'w-full px-3 py-2 border rounded-md',
        })
    )
    class Meta:
        model = Group
        fields = (
            'name', 'grade_level', 'schedule', 'academic_year',
            'max_students', 'description', 'subjects', 'teachers', 'status'
        )
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border rounded-md',
                'placeholder': 'Enter group name',
            }),
            'status': forms.Select(attrs={
                'class': 'w-full px-3 py-2 border rounded-md',
            }),
            'grade_level': forms.Select(attrs={
                'class': 'w-full px-3 py-2 border rounded-md',
            }),
            'schedule': forms.Select(attrs={
                'class': 'w-full px-3 py-2 border rounded-md',
            }),
            'academic_year': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border rounded-md',
                'placeholder': 'e.g., 2023-2024',
            }),
            'max_students': forms.NumberInput(attrs={
                'class': 'w-full px-3 py-2 border rounded-md',
                'placeholder': 'Enter maximum number of students',
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full px-3 py-2 border rounded-md',
                'placeholder': 'Enter group description',
                'rows': 4,
            }),
            'subjects': forms.CheckboxSelectMultiple(),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError("Group name is required.")
        return name

    def clean_grade_level(self):
        grade_level = self.cleaned_data.get('grade_level')
        if not grade_level:
            raise forms.ValidationError("Grade level is required.")
        return grade_level

    def clean_schedule(self):
        schedule = self.cleaned_data.get('schedule')
        if not schedule:
            raise forms.ValidationError("Schedule is required.")
        return schedule

    def clean_academic_year(self):
        academic_year = self.cleaned_data.get('academic_year')
        if not academic_year:
            raise forms.ValidationError("Academic year is required.")
        return academic_year

    def clean_max_students(self):
        max_students = self.cleaned_data.get('max_students')
        if max_students is None:
            raise forms.ValidationError("Maximum students is required.")
        return max_students

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if not description:
            raise forms.ValidationError("Description is required.")
        return description

    def clean_subjects(self):
        subjects = self.cleaned_data.get('subjects')
        if not subjects:
            raise forms.ValidationError("At least one subject must be selected.")
        return subjects

    def clean_teachers(self):
        teachers = self.cleaned_data.get('teachers')
        if not teachers:
            raise forms.ValidationError("At least one teacher must be selected.")
        return teachers