from django.db import models
from head_of_departments.models import HeadDepartment
from .base_models import BaseModel
from django.shortcuts import reverse
from django.conf import settings
from django.utils.text import slugify


class Department(BaseModel):
    STATUS_CHOICES = [
        ('ac', 'Active'),
        ('in', 'Inactive'),
        ('pd', 'Pending'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.TextField()
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=13)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='in')
    head_of_department = models.ForeignKey(HeadDepartment, on_delete=models.CASCADE, related_name='departments', null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Department, self).save(*args, **kwargs)

    def get_detail_url(self):
        return reverse('departments:detail', args=[
            self.created_at.year,
            self.created_at.month,
            self.created_at.day,
            self.slug
        ])

    def get_update_url(self):
        return reverse('departments:update', args=[self.pk])

    def get_delete_url(self):
        return reverse('departments:delete', args=[self.pk])

    def __str__(self):
        return f"{self.name}"