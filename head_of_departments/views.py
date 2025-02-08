from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import HeadDepartment
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import HeadOfDepartmentForm
from django.core.paginator import Paginator


class HeadOfDepartmentListView(ListView):
    model = HeadDepartment
    template_name = 'head_of_departments/list.html'
    context_object_name = 'heads'
    paginate_by = 10

    def get_queryset(self):
        heads = HeadDepartment.objects.all()
        status = self.request.GET.get('status')
        search_query = self.request.GET.get('search')

        if status:
            heads = heads.filter(status=status)
        if search_query:
            heads = heads.filter(name__icontains=search_query)
        return heads

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = self.request.GET.get('page')
        paginator = Paginator(self.get_queryset(), self.paginate_by)
        heads_page = paginator.get_page(page)

        context['heads'] = heads_page
        context['paginator'] = paginator
        return context


class HeadOfDepartmentCreateView(LoginRequiredMixin, CreateView):
    model = HeadDepartment
    form_class = HeadOfDepartmentForm
    template_name = 'head_of_departments/form.html'
    success_url = reverse_lazy('head_of_departments:list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class HeadOfDepartmentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = HeadDepartment
    form_class = HeadOfDepartmentForm
    template_name = 'head_of_departments/form.html'
    success_url = reverse_lazy('head_of_departments:list')
    context_object_name = 'head'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        head = self.get_object()
        return self.request.user == head.author

class HeadOfDepartmentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = HeadDepartment
    template_name = 'head_of_departments/confirm_delete.html'
    success_url = reverse_lazy('head_of_departments:list')

    def test_func(self):
        head = self.get_object()
        return self.request.user == head.author