from django.db import models
from subjects.models import Subject
from teachers.models import Teacher
from django.shortcuts import reverse
from django.conf import settings


class Group(models.Model):
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

    SCHEDULE_CHOICES = [
        ('mr', 'Morning Session'),
        ('af', 'Afternoon Session'),
        ('ev', 'Evening Session'),
    ]

    STATUS_CHOICES = [
        ('ac', 'Active'),
        ('in', 'Inactive'),
        ('pd', 'Pending'),
    ]

    name = models.CharField(max_length=100)
    academic_year = models.CharField(max_length=30)
    max_students = models.PositiveIntegerField()
    description = models.TextField()
    status =models.CharField(max_length=2, choices=STATUS_CHOICES)
    grade_level = models.CharField(max_length=2, choices=GRADE_LEVEL_CHOICES)
    schedule = models.CharField(max_length=2, choices=SCHEDULE_CHOICES, default='in')
    subjects = models.ManyToManyField(Subject, related_name='groups', blank=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='groups', blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


    def get_detail_url(self):
        return reverse('groups:detail', args=[self.pk])

    def get_update_url(self):
        return reverse('groups:update', args=[self.pk])

    def get_delete_url(self):
        return reverse('groups:delete', args=[self.pk])

    def __str__(self):
        return f"{self.name}"



