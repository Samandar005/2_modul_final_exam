from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Student
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import StudentForm
from groups.models import Group
from django.core.paginator import Paginator


class StudentListView(ListView):
    model = Student
    template_name = 'students/list.html'
    context_object_name = 'students'
    paginate_by = 10

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = self.request.GET.get('page')
        paginator = Paginator(self.get_queryset(), self.paginate_by)
        students_page = paginator.get_page(page)

        context['students'] = students_page
        context['paginator'] = paginator
        context['groups'] = Group.objects.all()
        return context


class StudentDetailView(DetailView):
    model = Student
    template_name = 'students/detail.html'
    context_object_name = 'student'

class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/form.html'
    success_url = reverse_lazy('students:list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class StudentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/form.html'
    success_url = reverse_lazy('students:list')
    context_object_name = 'student'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        student = self.get_object()
        return self.request.user == student.author

class StudentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Student
    template_name = 'students/confirm_delete.html'
    success_url = reverse_lazy('students:list')

    def test_func(self):
        student = self.get_object()
        return self.request.user == student.author
