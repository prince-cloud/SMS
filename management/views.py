from .models import *
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib.auth import get_user_model, logout
from django.views.generic import CreateView
from django.utils.decorators import method_decorator

# Create your views here.


def index(request):
    return render(request, 'index.html')

@login_required
def portal(request):
    return render(request, 'portal.html')

@login_required
def adminsite(request):
    return render(request, 'adminsite.html')

class AddStaff(CreateView):
    model = User
    form_class = AddStaff
    template_name = 'registration/addteacher.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return redirect('management:adminsite')


class AddStudent(CreateView):
    model = User
    form_class = AddStudent
    template_name = 'registration/addstudent.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return redirect('management:adminsite')

@login_required
def studentlist(request):
    students = Student.objects.all()
    user_type = "Student"
    context = {
        "students": students, 
        "user_type": user_type,
        }
    return render(request, 'studentlist.html', context)


def logoutview(request):
    logout(request)
    return redirect('management:portal')



