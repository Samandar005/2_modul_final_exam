from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Student
from .forms import StudentForm
from groups.models import Group


class StudentListView(ListView):
    model = Student
    template_name = 'students/list.html'
    context_object_name = 'students'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['groups'] = Group.objects.all()
        return ctx

    def get_queryset(self):
        students = Student.objects.all()
        status = self.request.GET.get('status')
        grade = self.request.GET.get('grade')
        group = self.request.GET.get('group')
        search_query = self.request.GET.get('search')

        if status:
            students = students.filter(status=status)
        if grade:
            students = students.filter(grade=grade)
        if group:
            students = students.filter(group=group)
        if search_query:
            students = students.filter(
                Q(first_name__icontains=search_query) | Q(last_name__icontains=search_query)
            )
        return students



class StudentDetailView(DetailView):
    model = Student
    template_name = 'students/detail.html'
    context_object_name = 'student'

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/form.html'
    success_url = reverse_lazy('students:list')

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/form.html'
    success_url = reverse_lazy('students:list')
    context_object_name = 'student'

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students/confirm_delete.html'
    success_url = reverse_lazy('students:list')

