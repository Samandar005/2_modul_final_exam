from django import forms
from .models import Subject

class SubjectForm(forms.ModelForm):
    prerequisites = forms.MultipleChoiceField(
        choices=Subject.PREREQUISITE_CHOICES,
        widget=forms.SelectMultiple(attrs={
            'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
        })
    )
    class Meta:
        model = Subject
        fields = ('name', 'department', 'description', 'credit_hours', 'grade_level', 'prerequisites', 'status')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter subject name',
            }),
            'department': forms.Select(attrs={
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
                'required': False,
            }),
            'status': forms.Select(attrs={
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter subject description',
                'rows': 4,
            }),
            'credit_hours': forms.NumberInput(attrs={
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter credit hheadours',
            }),
            'grade_level': forms.Select(attrs={
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
                'required': False,
            }),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 2:
            raise forms.ValidationError("Название предмета должно содержать не менее 2-х символов.")
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if len(description) < 10:
            raise forms.ValidationError("Описание предмета должно содержать не менее 10-ти символов.")
        return description

    def clean_credit_hours(self):
        credit_hours = self.cleaned_data.get('credit_hours')
        if credit_hours is None or credit_hours <= 0:
            raise forms.ValidationError("Количество кредитов должно быть положительным числом.")
        return credit_hours

    def clean_prerequisites(self):
        prerequisites = self.cleaned_data.get('prerequisites')
        if not prerequisites:
            raise forms.ValidationError("Пожалуйста, выберите требования.")
        return prerequisites