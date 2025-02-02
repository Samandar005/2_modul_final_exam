from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import SubjectForm
from .models import Subject


class SubjectListView(ListView):
    model = Subject
    template_name = 'subjects/list.html'
    context_object_name = 'subjects'

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
