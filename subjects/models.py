from django.db import models
from departments.base_models import BaseModel
from departments.models import Department
from django.shortcuts import reverse
from django.conf import settings
from django.utils.text import slugify
import re


class Subject(BaseModel):
    GRADE_LEVEL_CHOICES = [
        ('1', 'Grade 1'),
        ('2', 'Grade 2'),
        ('3', 'Grade 3'),
        ('4', 'Grade 4'),
        ('5', 'Grade 5'),
        ('6', 'Grade 6'),
        ('7', 'Grade 7'),
        ('8', 'Grade 8'),
        ('9', 'Grade 9'),
        ('10', 'Grade 10'),
        ('11', 'Grade 11'),
        ('12', 'Grade 12'),
    ]

    PREREQUISITE_CHOICES = [
        ('Basic Mathematics', 'Basic Mathematics'),
        ('Introduction to Physics', 'Introduction to Physics'),
        ('Basic Chemistry', 'Basic Chemistry'),
        ('English Language', 'English Language'),
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
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='subjects', null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Subject, self).save(*args, **kwargs)

    def get_detail_url(self):
        return reverse('subjects:detail', args=[
            self.created_at.year,
            self.created_at.month,
            self.created_at.day,
            self.slug
        ])

    @property
    def prerequisite_list(self):
        if not self.prerequisites:
            return []
        return re.sub(r"[\[\]']", "", self.prerequisites).split(',')

    def get_update_url(self):
        return reverse('subjects:update', args=[self.pk])

    def get_delete_url(self):
        return reverse('subjects:delete', args=[self.pk])

    def __str__(self):
        return f"{self.name}"
