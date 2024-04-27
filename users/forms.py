from django import forms
from . models import User,Parent, Student, Admin, Teacher
from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordResetForm,SetPasswordForm
from django.contrib.auth.models import User

class ParentForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields = ['user', 'father_name', 'mother_name', 'father_occupation', 'mother_occupation', 'father_phone', 'school', 'profile_pic']


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['user', 'roll_number', 'standard', 'section', 'parent', 'school', 'profile_pic']

    
class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = ['user', 'school']


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['user', 'school', 'qualification', 'experience', 'joining_date', 'profile_pic']




class CustomAuthenticationForm(AuthenticationForm):
   def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       for field in self.fields.values():
           field.widget.attrs['class'] = 'form-control'
  




class CustomPasswordResetForm(PasswordResetForm):
   def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       for field in self.fields.values():
           field.widget.attrs['class'] = 'form-control'


class CustomPasswordSetForm(SetPasswordForm):
   def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       for field in self.fields.values():
           field.widget.attrs['class'] = 'form-control'
