from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from departments.models import Department
from .forms import SubjectForm
from .models import Subject


class SubjectListView(ListView):
    model = Subject
    template_name = 'subjects/list.html'
    context_object_name = 'subjects'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['departments'] = Department.objects.all()
        return ctx

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


class SubjectDetailView(DetailView):
    model = Subject
    template_name = 'subjects/detail.html'
    context_object_name = 'subject'

class SubjectCreateView(CreateView):
    model = Subject
    form_class = SubjectForm
    template_name = 'subjects/form.html'
    success_url = reverse_lazy('subjects:list')

class SubjectUpdateView(UpdateView):
    model = Subject
    form_class = SubjectForm
    template_name = 'subjects/form.html'
    success_url = reverse_lazy('subjects:list')

class SubjectDeleteView(DeleteView):
    model = Subject
    template_name = 'subjects/confirm_delete.html'
    success_url = reverse_lazy('subjects:list')
