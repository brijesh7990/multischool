from django import forms

from school.models import Section, Standard
from .models import User, Parent, Student, Admin, Teacher
from django.contrib.auth import get_user_model
from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import password_validation
from django.contrib.auth.forms import (
    AuthenticationForm,
    UsernameField,
    PasswordResetForm,
    SetPasswordForm,
)


class UsersForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ["username", "email", "password"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"


class ParentForm(forms.ModelForm):
    # user = forms.ModelChoiceField(queryset=Parent.objects.all())
    # profile_pic = forms.ImageField()

    class Meta:
        model = Parent
        fields = [
            # "user",
            "father_name",
            "mother_name",
            "father_occupation",
            "mother_occupation",
            "father_phone",
            # "school",
            "profile_pic",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"


class StudentForm(forms.ModelForm):
    standard = forms.ModelChoiceField(queryset=Standard.objects.none())
    section = forms.ModelChoiceField(queryset=Standard.objects.none())
    class Meta:
        model = Student
        fields = [
            # "user",
            "roll_number",
            "standard",
            "section",
            "parent",
            # "school",
            "profile_pic",
        ]

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['standard'].queryset = Standard.objects.filter(school=user.admin.school)
        self.fields["section"].queryset = Section.objects.filter(school=user.admin.school)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"


class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = ["user", "school"]


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = [
            "user",
            "school",
            "qualification",
            "experience",
            "joining_date",
            "profile_pic",
        ]


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"


class CustomPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"


class CustomPasswordSetForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
