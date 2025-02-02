from django.db import models
from departments.base_models import BaseModel
from departments.models import Department


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

    name = models.CharField(max_length=200)
    department = models.ForeignKey(Department,  on_delete=models.CASCADE, related_name='subjects', null=True, blank=True)
    description = models.TextField()
    credit_hours = models.PositiveIntegerField()
    grade_level = models.CharField(max_length=2, choices=GRADE_LEVEL_CHOICES)
    prerequisites = models.CharField(max_length=9, choices=PREREQUISITE_CHOICES)

