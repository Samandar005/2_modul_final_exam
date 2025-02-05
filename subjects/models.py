from django.db import models
from departments.base_models import BaseModel
from departments.models import Department
from django.shortcuts import reverse


class Subject(BaseModel):
    GRADE_LEVEL_CHOICES = [
        ('9', 'Grade 9'),
        ('10', 'Grade 10'),
        ('11', 'Grade 11'),
        ('12', 'Grade 12'),
    ]

    PREREQUISITE_CHOICES = [
        ('math', 'Basic Mathematics'),
        ('physics', 'Introduction to Physics'),
        ('chemistry', 'Basic Chemistry'),
        ('english', 'English Language'),
    ]

    STATUS_CHOICES = [
        ('ac', 'Active'),
        ('in', 'Inactive'),
        ('pd', 'Pending'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField()
    credit_hours = models.PositiveIntegerField()
    prerequisites = models.CharField(max_length=255, blank=True)
    grade_level = models.CharField(max_length=2, choices=GRADE_LEVEL_CHOICES)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='in')
    department = models.ForeignKey(Department,  on_delete=models.CASCADE, related_name='subjects', null=True, blank=True)


    @property
    def prerequisite_list(self):
        return [prerequisite.strip() for prerequisite in self.prerequisites.split(',')] if self.prerequisites else []

    def get_detail_url(self):
        return reverse('subjects:detail', args=[self.pk])

    def get_update_url(self):
        return reverse('subjects:update', args=[self.pk])

    def get_delete_url(self):
        return reverse('subjects:delete', args=[self.pk])

    def __str__(self):
        return f"{self.name}"
