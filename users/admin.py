from django.contrib import admin

from users.models import Admin, Parent, Student, Teacher, User

# Register your models here.

admin.site.register(User)
admin.site.register(Student)
admin.site.register(Parent)
admin.site.register(Teacher)
admin.site.register(Admin)
