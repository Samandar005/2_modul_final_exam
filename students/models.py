from django.db import models
from django.db.models import CASCADE
from django.utils.http import content_disposition_header

from departments.base_models import BaseModel
from groups.models import Group
from django.shortcuts import reverse


class Student(BaseModel):
    SELECT_GENDER = [
        ('mal', 'Male'),
        ('fem', 'Female'),
    ]

    GRADE_CHOICES = [
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

    STATUS_CHOICES = [
        ('ac', 'Active'),
        ('in', 'Inactive'),
        ('pd', 'Pending'),
    ]


    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=150)
    dob = models.DateField()
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=13)
    address = models.TextField()
    parent_name = models.CharField(max_length=100)
    parent_phone_number = models.CharField(max_length=13)
    parent_email = models.EmailField(unique=True)
    image = models.ImageField(upload_to='students/')
    grade = models.CharField(max_length=2, choices=GRADE_CHOICES)
    gender = models.CharField(max_length=3, choices=SELECT_GENDER)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='in')
    group = models.ForeignKey(Group, on_delete=CASCADE, related_name='students', blank=True)

    def get_detail_url(self):
        return reverse('students:detail', args=[self.pk])

    def get_update_url(self):
        return reverse('students:update', args=[self.pk])

    def get_delete_url(self):
        return reverse('students:delete', args=[self.pk])

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

