from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Teacher
from .forms import TeacherForm


class TeacherListView(ListView):
    model = Teacher
    template_name = 'teachers/list.html'
    context_object_name = 'teachers'

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

class TeacherDeleteView(DeleteView):
    model = Teacher
    template_name = 'teachers/confirm_delete.html'
    success_url = reverse_lazy('teachers:list')