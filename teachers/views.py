from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from departments.models import Department
from subjects.models import Subject
from .models import Teacher
from .forms import TeacherForm
from django.db.models import Q


class TeacherListView(ListView):
    model = Teacher
    template_name = 'teachers/list.html'
    context_object_name = 'teachers'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['departments'] = Department.objects.all()
        ctx['subjects'] = Subject.objects.all()
        return ctx

    def get_queryset(self):
        teachers = Teacher.objects.all()
        status = self.request.GET.get('status')
        department = self.request.GET.get('department')
        subjects = self.request.GET.get('subject')
        search_query = self.request.GET.get('search')

        if status:
            teachers = teachers.filter(status=status)
        if department:
            teachers = teachers.filter(department=department)
        if subjects:
            teachers = teachers.filter(subjects=subjects)
        if search_query:
            teachers = teachers.filter(
                Q(first_name__icontains=search_query) |
                Q(last_name__icontains=search_query)
            )
        return teachers

class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'teachers/detail.html'
    context_object_name = 'teacher'

class TeacherCreateView(CreateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'teachers/form.html'
    success_url = reverse_lazy('teachers:list')

class TeacherUpdateView(UpdateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'teachers/form.html'
    success_url = reverse_lazy('teachers:list')
    context_object_name = 'teacher'

class TeacherDeleteView(DeleteView):
    model = Teacher
    template_name = 'teachers/confirm_delete.html'
    success_url = reverse_lazy('teachers:list')