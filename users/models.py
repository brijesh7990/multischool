from django.db import models
from django.contrib.auth.models import AbstractUser
from base.models import BaseModel

# Create your models here.


class User(AbstractUser, BaseModel):
    ADMIN = "admin"
    TEACHER = "teacher"
    STUDENT = "student"
    PARENT = "parent"
    SUPERADMIN = "superadmin"
    USER_TYPE_CHOICES = [
        (SUPERADMIN, "Superadmin"),
        (ADMIN, "admin"),
        (TEACHER, "teacher"),
        (STUDENT, "student"),
        (PARENT, "parent"),
    ]
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=15, choices=USER_TYPE_CHOICES)
    phone = models.CharField(max_length=10)
    address = models.TextField()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "password"]

    def __str__(self):
        return self.email


class Student(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_number = models.CharField(max_length=10)
    standard = models.ForeignKey("school.Standard", on_delete=models.CASCADE)
    section = models.ForeignKey("school.Section", on_delete=models.CASCADE)
    parent = models.ForeignKey("Parent", on_delete=models.CASCADE)
    school = models.ForeignKey("school.School", on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to="media/student/profile_pic/")

    def __str__(self):
        return self.user.email


class Parent(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    father_occupation = models.CharField(max_length=100)
    mother_occupation = models.CharField(max_length=100)
    father_phone = models.CharField(max_length=10)
    school = models.ForeignKey("school.School", on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to="media/parent/profile_pic/")

    def __str__(self):
        return self.user.email


class Teacher(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school = models.ForeignKey("school.School", on_delete=models.CASCADE)
    qualification = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    joining_date = models.DateField()
    profile_pic = models.ImageField(upload_to="media/teacher/profile_pic/")

    def __str__(self):
        return self.user.email

class Admin(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school = models.ForeignKey("school.School", on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email
