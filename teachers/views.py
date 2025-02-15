from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from departments.models import Department
from subjects.models import Subject
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Teacher
from .forms import TeacherForm
from django.db.models import Q
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from students.models import Student

class TeacherListView(LoginRequiredMixin, ListView):
    model = Teacher
    template_name = 'teachers/list.html'
    context_object_name = 'teachers'
    paginate_by = 10

    def get_queryset(self):
        teachers = Teacher.objects.all()
        status = self.request.GET.get('status')
        department = self.request.GET.get('department')
        subject = self.request.GET.get('subject')
        search_query = self.request.GET.get('search')

        if status:
            teachers = teachers.filter(status=status)
        if department:
            teachers = teachers.filter(department=department)
        if subject:
            teachers = teachers.filter(subjects=subject)
        if search_query:
            teachers = teachers.filter(
                Q(first_name__icontains=search_query) | Q(last_name__icontains=search_query)
            )

        return teachers

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = self.request.GET.get('page')
        paginator = Paginator(self.get_queryset(), self.paginate_by)
        teachers_page = paginator.get_page(page)

        context['teachers'] = teachers_page
        context['paginator'] = paginator
        context['departments'] = Department.objects.all()
        context['subjects'] = Subject.objects.all()
        return context


class TeacherDetailView(LoginRequiredMixin, DetailView):
    model = Teacher
    template_name = 'teachers/detail.html'
    context_object_name = 'teacher'

    def get_object(self, queryset=None):
        return get_object_or_404(Teacher, slug=self.kwargs.get('slug'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        teacher = self.get_object()
        students = Student.objects.filter(group__in=teacher.groups.all()).distinct()
        context['students'] = students
        context['total_students'] = students.count()
        return context


class TeacherCreateView(LoginRequiredMixin, CreateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'teachers/form.html'
    success_url = reverse_lazy('teachers:list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class TeacherUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'teachers/form.html'
    success_url = reverse_lazy('teachers:list')
    context_object_name = 'teacher'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        teacher = self.get_object()
        return self.request.user == teacher.author

class TeacherDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Teacher
    template_name = 'teachers/confirm_delete.html'
    success_url = reverse_lazy('teachers:list')

    def test_func(self):
        teacher = self.get_object()
        return self.request.user == teacher.author
