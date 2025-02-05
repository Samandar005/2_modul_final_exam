from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import HeadDepartment
from .forms import HeadOfDepartmentForm


class HeadOfDepartmentListView(ListView):
    model = HeadDepartment
    template_name = 'head_of_departments/list.html'
    context_object_name = 'heads'

class HeadOfDepartmentCreateView(CreateView):
    model = HeadDepartment
    form_class = HeadOfDepartmentForm
    template_name = 'head_of_departments/form.html'
    success_url = reverse_lazy('head_of_departments:list')

class HeadOfDepartmentUpdateView(UpdateView):
    model = HeadDepartment
    form_class = HeadOfDepartmentForm
    template_name = 'head_of_departments/form.html'
    success_url = reverse_lazy('head_of_departments:list')
    context_object_name = 'head'


class HeadOfDepartmentDeleteView(DeleteView):
    model = HeadDepartment
    template_name = 'head_of_departments/confirm_delete.html'
    success_url = reverse_lazy('head_of_departments:list')

