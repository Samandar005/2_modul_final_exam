from django.db import models
from departments.base_models import BaseModel

class HeadDepartment(BaseModel):
    name = models.CharField(max_length=200)
