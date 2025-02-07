from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from sqlparse.engine.grouping import group_if

from teachers.models import Teacher
from .models import Group
from .forms import GroupForm


class GroupListView(ListView):
    model = Group
    template_name = 'groups/list.html'
    context_object_name = 'groups'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['teachers'] = Teacher.objects.all()
        return ctx

    def get_queryset(self):
        groups = Group.objects.all()
        grade_level = self.request.GET.get('grade_level')
        status = self.request.GET.get('status')
        teacher = self.request.GET.get('teacher')
        search_query = self.request.GET.get('search')

        if grade_level:
            groups = groups.filter(grade_level=grade_level)
        if status:
            groups = groups.filter(status=status)
        if teacher:
            groups = groups.filter(teacher=teacher)
        if search_query:
            groups = groups.filter(name__icontains=search_query)
        return groups

class GroupDetailView(DetailView):
    model = Group
    template_name = 'groups/detail.html'
    context_object_name = 'group'

class GroupCreateView(CreateView):
    model = Group
    form_class = GroupForm
    template_name = 'groups/form.html'
    success_url = reverse_lazy('groups:list')

class GroupUpdateView(UpdateView):
    model = Group
    form_class = GroupForm
    template_name = 'groups/form.html'
    success_url = reverse_lazy('groups:list')
    context_object_name = 'group'


class GroupDeleteView(DeleteView):
    model = Group
    template_name = 'groups/confirm_delete.html'
    success_url = reverse_lazy('groups:list')
