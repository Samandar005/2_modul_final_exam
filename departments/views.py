from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Department
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import DepartmentForm
from head_of_departments.models import HeadDepartment
from teachers.models import Teacher
from students.models import Student
from groups.models import Group
from subjects.models import Subject


class HomePageView(ListView):
    model = Student
    template_name = 'dashboard.html'
    context_object_name = 'students'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['teachers'] = Teacher.objects.all()
        ctx['groups'] = Group.objects.all()
        ctx['subjects'] = Subject.objects.all()
        ctx['groups_count'] = Group.objects.filter(status='ac').count()
        ctx['subject_names'] = [subject.name for subject in Subject.objects.all()]
        ctx['subject_teachers_counts'] = [subject.teachers.count() for subject in Subject.objects.all()]
        return ctx


class DepartmentListView(ListView):
    model = Department
    template_name = 'departments/list.html'
    context_object_name = 'departments'
    paginate_by = 10

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = self.request.GET.get('page')
        paginator = Paginator(self.get_queryset(), self.paginate_by)
        departments_page = paginator.get_page(page)

        context['departments'] = departments_page
        context['paginator'] = paginator
        context['heads'] = HeadDepartment.objects.all()
        return context

class DepartmentDetailView(DetailView):
    model = Department
    template_name = 'departments/detail.html'
    context_object_name = 'department'

    def get_object(self, queryset=None):
        return get_object_or_404(Department, slug=self.kwargs.get('slug'))

class DepartmentCreateView(LoginRequiredMixin, CreateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'departments/form.html'
    success_url = reverse_lazy('departments:list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class DepartmentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'departments/form.html'
    success_url = reverse_lazy('departments:list')
    context_object_name = 'department'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        department = self.get_object()
        return self.request.user == department.author

class DepartmentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Department
    template_name = 'departments/confirm_delete.html'
    success_url = reverse_lazy('departments:list')

    def test_func(self):
        department = self.get_object()
        return self.request.user == department.author
