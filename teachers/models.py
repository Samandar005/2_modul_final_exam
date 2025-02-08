from django.db import models
from django.shortcuts import reverse
from departments.base_models import BaseModel
from departments.models import Department
from subjects.models import Subject
from django.conf import settings


class Teacher(BaseModel):
    EMPLOYMENT_TYPE_CHOICES = [
        ('full', 'Full Time'),
        ('part', 'Part Time'),
        ('contract', 'Contract'),
    ]

    STATUS_CHOICES = [
        ('ac', 'Active'),
        ('in', 'Inactive'),
        ('pd', 'Pending'),
    ]

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    qualification = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=13)
    address = models.TextField()
    join_date = models.DateField()
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='teachers/')
    employment_type = models.CharField(max_length=8, choices=EMPLOYMENT_TYPE_CHOICES)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='in')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='teachers', null=True, blank=True)
    subjects = models.ManyToManyField(Subject, related_name='teachers', blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def get_detail_url(self):
        return reverse('teachers:detail', args=[self.pk])

    def get_update_url(self):
        return reverse('teachers:update', args=[self.pk])

    def get_delete_url(self):
        return reverse('teachers:delete', args=[self.pk])

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

