from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from teachers.models import Teacher
from .models import Group
from django.shortcuts import get_object_or_404
from .forms import GroupForm
from django.core.paginator import Paginator


class GroupListView(ListView):
    model = Group
    template_name = 'groups/list.html'
    context_object_name = 'groups'
    paginate_by = 10

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = self.request.GET.get('page')
        paginator = Paginator(self.get_queryset(), self.paginate_by)
        groups_page = paginator.get_page(page)

        context['groups'] = groups_page
        context['paginator'] = paginator
        context['teachers'] = Teacher.objects.all()
        return context


class GroupDetailView(DetailView):
    model = Group
    template_name = 'groups/detail.html'
    context_object_name = 'group'

    def get_object(self, queryset=None):
        return get_object_or_404(Group, slug=self.kwargs.get('slug'))

class GroupCreateView(LoginRequiredMixin, CreateView):
    model = Group
    form_class = GroupForm
    template_name = 'groups/form.html'
    success_url = reverse_lazy('groups:list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class GroupUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Group
    form_class = GroupForm
    template_name = 'groups/form.html'
    success_url = reverse_lazy('groups:list')
    context_object_name = 'group'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        group = self.get_object()
        return self.request.user == group.author

class GroupDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Group
    template_name = 'groups/confirm_delete.html'
    success_url = reverse_lazy('groups:list')

    def test_func(self):
        group = self.get_object()
        return self.request.user == group.author