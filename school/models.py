from django.db import models
from users.models import *
from base.models import BaseModel

# Create your models here.


class School(BaseModel):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    website = models.URLField()
    logo = models.ImageField(upload_to="media/school/logo/")

    def __str__(self):
        return self.name


class Standard(BaseModel):
    name = models.CharField(max_length=50)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Section(BaseModel):
    name = models.CharField(max_length=50)
    standard = models.ForeignKey(Standard, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return f"standard: {self.standard} section: {self.name}"
