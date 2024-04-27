from django.contrib import admin

from school.models import School, Section, Standard

# Register your models here.
admin.site.register(School)
admin.site.register(Standard)
admin.site.register(Section)
