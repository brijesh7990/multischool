from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User, Group


from users.forms import ParentForm, UsersForm
from .models import User, Student, Parent, Teacher
from django.views.generic import CreateView
from django.contrib import messages
from django.contrib.auth import get_user_model
# Create your views here.


class AdminOrSuperUserMixin(UserPassesTestMixin):
    def test_func(self):
        return any(
            [
                self.request.user.role == User.SUPERADMIN,
                self.request.user.role == User.ADMIN,
                self.request.user.has_perm("users.add_parent"),
            ]
        )


class ParentCreateView(AdminOrSuperUserMixin, LoginRequiredMixin, CreateView):
    model = Parent
    template_name = "users/parent_form.html"
    form_class = ParentForm
    group = Group.objects.get(name="ParentGroup")


    def get_context_data(self, *args, **kwargs):
        context_data = super(ParentCreateView, self).get_context_data(*args, **kwargs)
        context_data["userform"] = UsersForm(self.request.POST or None, self.request.FILES or None)
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
        return render(self.request, self.template_name, {"form": form, "userform": userform})
        
    
    

    
    
    
