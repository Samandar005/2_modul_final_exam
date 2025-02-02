from django.db import models
from django.db.models import CASCADE, ManyToManyField
from subjects.models import Subject
from teachers.models import Teacher


class Group(models.Model):
    GRADE_LEVEL_CHOICES = [
        ('9', 'Grade 9'),
        ('10', 'Grade 10'),
        ('11', 'Grade 11'),
        ('12', 'Grade 12'),
    ]

    SCHEDULE_CHOICES = [
        ('mr', 'Morning Session'),
        ('af', 'Afternoon Session'),
        ('ev', 'Evening Session'),
    ]

    name = models.CharField(max_length=100)
    grade_level = models.CharField(max_length=2, choices=GRADE_LEVEL_CHOICES)
    teacher = models.OneToOneField(Teacher, on_delete=CASCADE, related_name='group', null=True, blank=True)
    schedule = models.CharField(max_length=2, choices=SCHEDULE_CHOICES)
    academic_year = models.CharField(max_length=30)
    max_students = models.PositiveIntegerField()
    description = models.TextField()
    subjects = ManyToManyField(Subject, related_name='groups')



