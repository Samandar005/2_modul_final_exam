from django.db import models

from departments.base_models import BaseModel
from departments.models import Department
from subjects.models import Subject


class Teacher(BaseModel):
    EMPLOYMENT_TYPE_CHOICES = [
        ('full', 'Full Time'),
        ('part', 'Part Time'),
        ('contract', 'Contract'),
    ]

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='teachers', null=True, blank=True)
    subjects = models.ManyToManyField(Subject, related_name='teachers', null=True, blank=True)
    qualification = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=13)
    address = models.TextField()
    join_date = models.DateField()
    employment_type = models.CharField(max_length=8, choices=EMPLOYMENT_TYPE_CHOICES)
    image = models.ImageField(upload_to='teachers/')
