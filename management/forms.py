from django import forms
from .models import *
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm


class AddStaff(UserCreationForm):

    firstname = forms.CharField(max_length=30,
                                widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control', }), label="Firstname",)

    lastname = forms.CharField(max_length=30,
                               widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control', }), label="Lastname",)

    phone = forms.CharField(max_length=10,
                            widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control', }), label="Mobile No.",)

    address = forms.CharField(max_length=30,
                              widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control', }), label="Address",)

    sex = forms.CharField(
        widget=forms.Select(choices=SEX, attrs={'class': 'browser-default custom-select'})
    )
    
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic()
    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data.get('username')
        user.first_name = self.cleaned_data.get('firstname')
        user.last_name = self.cleaned_data.get('lastname')
        user.phone = self.cleaned_data.get('phone')
        user.email = self.cleaned_data.get('email')
        user.address = self.cleaned_data.get('address')
        user.is_teacher = True
        if commit:
            user.save()
        return user


class AddStudent(UserCreationForm):
    username = forms.CharField(max_length=30,
                               widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control', }), label="Username",)

    address = forms.CharField(max_length=30,
                              widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control', }), label="Address",)

    phone = forms.CharField(
        max_length=10,
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control', }), label="Guidian Phone",)

    firstname = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control', }), label="Firstname",)

    lastname = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control', }), label="Lastname",
    )

    stage = forms.CharField(
        widget=forms.Select(choices=CLASS, attrs={'class': 'browser-default custom-select', }),
    )

    sex = forms.CharField(
        widget=forms.Select(choices=SEX, attrs={'class': 'browser-default custom-select'})
    )

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic()
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.first_name = self.cleaned_data.get('firstname')
        user.last_name = self.cleaned_data.get('lastname')
        user.phone = self.cleaned_data.get('phone')
        user.email = self.cleaned_data.get('email')
        user.save()
        student = Student.objects.create(
            user=user, id_number=user.username, stage=self.cleaned_data.get('class'))
        student.save()
        return user
