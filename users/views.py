from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User, Group


from users.forms import ParentForm, StudentForm, UsersForm
from users.permissions import AdminOrSuperUserMixin

from .models import User, Student, Parent, Teacher
from django.views.generic import CreateView
from django.contrib import messages
from django.contrib.auth import get_user_model

# Create your views here.




class ParentCreateView(AdminOrSuperUserMixin, LoginRequiredMixin, CreateView):
    model = Parent
    template_name = "users/parent_form.html"
    form_class = ParentForm
    group = Group.objects.get(name="ParentGroup")

    def get_context_data(self, *args, **kwargs):
        context_data = super(ParentCreateView, self).get_context_data(*args, **kwargs)
        context_data["userform"] = UsersForm(
            self.request.POST or None, self.request.FILES or None
        )
        return context_data

    def post(self, form):
        print("self.group", self.group)
        form = self.get_form()
        userform = UsersForm(self.request.POST, self.request.FILES)
        if form.is_valid() and userform.is_valid():
            user = userform.save(commit=False)
            user.set_password(user.password)
            user.role = User.PARENT
            user.save()
            user.groups.add(self.group)
            user.save()
            parent = form.save(commit=False)
            parent.user = user
            parent.school = self.request.user.admin.school
            parent.save()
            messages.success(self.request, "Parent Created Successfully")
        return render(
            self.request, self.template_name, {"form": form, "userform": userform}
        )


class StudentCreateView(AdminOrSuperUserMixin, LoginRequiredMixin, CreateView):
    template_name = "users/student_form.html"
    form_class = StudentForm
    group = Group.objects.get(name="StudentGroup")

    def get_context_data(self, **kwargs):
        context_data = {"form": self.form_class(self.request.user, data=self.request.POST or None, files=self.request.FILES or None)}
        context_data["userform"] = UsersForm(
            self.request.POST or None, self.request.FILES or None
        )
        return context_data
    
    def post(self, request, *args, **kwargs):
        form = StudentForm(self.request.user, data=self.request.POST, files = self.request.FILES)
        userform = UsersForm(self.request.POST, self.request.FILES)
        if form.is_valid() and userform.is_valid():
            user = userform.save(commit = False)
            user.set_password(user.password)
            user.role = User.STUDENT
            user.save()
            user.groups.add(self.group)
            user.is_staff = True
            user.save()
            student = form.save(commit = False)
            student.user = user
            student.school = self.request.user.admin.school
            student.save()
            messages.success(self.request, f"Student- {user.email} Created Successfully")
            return redirect("studentcreate")
        return render(request, self.template_name, {"form": form, "userform": userform})


