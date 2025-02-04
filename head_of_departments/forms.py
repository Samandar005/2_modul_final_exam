from django import forms
from .models import HeadDepartment


class HeadOfDepartmentForm(forms.ModelForm):
    class Meta:
        model = HeadDepartment
        fields = ('name',)
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter Head of Department name',
            })
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 2:
            raise forms.ValidationError("Название предмета должно содержать не менее 2-х символов.")
        return name