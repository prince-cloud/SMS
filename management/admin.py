from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import *
# Register your models here.


admin.site.register(Student)
#admin.site.register(Staff)
admin.site.register(User)
#admin.site.register(Subject)
#admin.site.register(SubjectAllocation)
#admin.site.register(Term)
#admin.site.register(Result)
#admin.site.register(RepeatedStudent)