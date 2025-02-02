from django.db import models
from head_of_departments.models import HeadDepartment
from .base_models import BaseModel

class Department(BaseModel):
    name = models.CharField(max_length=100)
    head_of_department = models.ForeignKey(HeadDepartment, on_delete=models.CASCADE, related_name='departments', null=True, blank=True)
    description = models.TextField()
    location = models.TextField()
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=13)

    def __str__(self):
        return f"{self.name}"