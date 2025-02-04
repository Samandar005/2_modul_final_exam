from django.db import models
from departments.base_models import BaseModel
from django.shortcuts import reverse


class HeadDepartment(BaseModel):
    name = models.CharField(max_length=200)

    def get_update_url(self):
        return reverse('head_of_departments:update', args=[self.pk])

    def get_delete_url(self):
        return reverse('head_of_departments:delete', args=[self.pk])

    def __str__(self):
        return f"{self.name}"