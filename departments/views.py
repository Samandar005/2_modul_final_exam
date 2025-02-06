from re import search

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views import  View
from .models import Department
from .forms import DepartmentForm
from head_of_departments.models import HeadDepartment


class HomePageView(View):
    def get(self, request):
        return render(request, 'dashboard.html')

class DepartmentListView(ListView):
    model = Department
    template_name = 'departments/list.html'
    context_object_name = 'departments'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heads'] = HeadDepartment.objects.all()
        return context

    def get_queryset(self):
        departments = Department.objects.all()
        head_of_department = self.request.GET.get('head_of_department')
        status = self.request.GET.get('status')
        search_query = self.request.GET.get('search')

        if head_of_department:
            departments = departments.filter(head_of_department=head_of_department)
        if status:
            departments = departments.filter(status=status)
        if search_query:
            departments = departments.filter(name__icontains=search_query)

        return departments


class DepartmentDetailView(DetailView):
    model = Department
    template_name = 'departments/detail.html'
    context_object_name = 'department'

class DepartmentCreateView(CreateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'departments/form.html'
    success_url = reverse_lazy('departments:list')

class DepartmentUpdateView(UpdateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'departments/form.html'
    success_url = reverse_lazy('departments:list')
    context_object_name = 'department'

class DepartmentDeleteView(DeleteView):
    model = Department
    template_name = 'departments/confirm_delete.html'
    success_url = reverse_lazy('departments:list')
