from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from departments.models import Department
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import SubjectForm
from .models import Subject
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from students.models import Student


class SubjectListView(ListView):
    model = Subject
    template_name = 'subjects/list.html'
    context_object_name = 'subjects'
    paginate_by = 10

    def get_queryset(self):
        subjects = Subject.objects.all()
        status = self.request.GET.get('status')
        department = self.request.GET.get('department')
        grade_level = self.request.GET.get('grade_level')
        search_query = self.request.GET.get('search')

        if status:
            subjects = subjects.filter(status=status)
        if department:
            subjects = subjects.filter(department=department)
        if grade_level:
            subjects = subjects.filter(grade_level=grade_level)
        if search_query:
            subjects = subjects.filter(name__icontains=search_query)

        return subjects

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = self.request.GET.get('page')
        paginator = Paginator(self.get_queryset(), self.paginate_by)
        subjects_page = paginator.get_page(page)

        context['subjects'] = subjects_page
        context['paginator'] = paginator
        context['departments'] = Department.objects.all()
        return context

class SubjectDetailView(DetailView):
    model = Subject
    template_name = 'subjects/detail.html'
    context_object_name = 'subject'

    def get_object(self, queryset=None):
        return get_object_or_404(Subject, slug=self.kwargs.get('slug'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subject = self.get_object()
        students = Student.objects.filter(group__in=subject.groups.all()).distinct()
        context['total_students'] = students.count()
        return context

class SubjectCreateView(LoginRequiredMixin, CreateView):
    model = Subject
    form_class = SubjectForm
    template_name = 'subjects/form.html'
    success_url = reverse_lazy('subjects:list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class SubjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Subject
    form_class = SubjectForm
    template_name = 'subjects/form.html'
    success_url = reverse_lazy('subjects:list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        subject = self.get_object()
        return self.request.user == subject.author

class SubjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Subject
    template_name = 'subjects/confirm_delete.html'
    success_url = reverse_lazy('subjects:list')

    def test_func(self):
        subject = self.get_object()
        return self.request.user == subject.author