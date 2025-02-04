from django.db import models
from head_of_departments.models import HeadDepartment
from .base_models import BaseModel
from django.shortcuts import reverse


class Department(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.TextField()
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=13)
    head_of_department = models.ForeignKey(HeadDepartment, on_delete=models.CASCADE, related_name='departments', null=True, blank=True)

    def get_detail_url(self):
        return reverse('departments:detail', args=[self.pk])

    def get_update_url(self):
        return reverse('departments:update', args=[self.pk])

    def get_delete_url(self):
        return reverse('departments:delete', args=[self.pk])

    def __str__(self):
        return f"{self.name}"