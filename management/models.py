from django.db import models
from django.contrib.auth.models import User, AbstractUser, BaseUserManager, AbstractBaseUser, UserManager
from .validators import ASCIIUsernameValidator
from django.conf import settings

#from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
#from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

#from .managers import UserManager

# Create your models here.
SEX = (
    ('M', 'M'),
    ('F', 'F'),
)

CLASS = (
    ('Nursery One', 'Nursery One'),
    ('Nursery Two', 'Nursery Two'),
    ('K. G 1', 'K.G One'),
    ('K. G 2', 'K.G Two'),
    ('Stage 1', 'Stage 1'),
    ('Stage 2', 'Stage 2'),
    ('Stage 3', 'Stage 3'),
    ('Stage 4', 'Stage 4'),
    ('Stage 5', 'Stage 5'),
    ('Stage 6', 'Stage 6'),
    ('Form 1', 'Form One'),
    ('Form 2', 'Form Two'),
    ('Form 3', 'Form Three'),
)

STATUS = (
    ('HEADMASTER', 'HEAD MASTER'),
    ('STAFF', 'STAFF'),
    ('MENTEE', 'MENTEE'),
    ('NABCO', 'NABCO'),
    ('INTERN', 'INTERN'),
)

TERM = (
    ('FIRST TERM', 'FIRST TERM'),
    ('SECOND TERM', 'SECOND TERM'),
    ('THIRD TERM', 'THIRD TERM'),
)


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    phone = models.CharField(max_length=10, blank=True, null=True)
    address = models.CharField(max_length=60, blank=True, null=True)
    picture = models.ImageField(upload_to="pictures/", blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    sex = models.CharField(choices=SEX, max_length=2)


    def get_picture(self):
        no_picture = settings.STATIC_URL + 'img/img_avatar.png'
        try:
            return self.picture.url
        except:
            return no_picture

    def get_full_name(self):
        full_name = self.username
        if self.first_name and self.last_name:
            full_name = self.first_name + " " + self.last_name
        return full_name


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id_number = models.CharField(max_length=20, unique=True)
    stage = models.CharField(choices=CLASS, max_length=20)

    def __str__(self):
        return self.user.last_name + " " + self.user.last_name

    def get_absolute_url(self):
        return reverse('profile')


""" class Subject(models.Model):
    subject_name = models.CharField(
        max_length=60, blank=False, null=False, unique=True)
    description = models.CharField(max_length=500)
    elective = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.subject_name
 """

""" class SubjectAllocation(models.Model):
    staff = models.ForeignKey(User, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject, related_name='allocated_course')

    def __str__(self):
        return self.staff.first_name

 """
""" class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ManyToManyField(Subject)
    mark = models.DecimalField(decimal_places=2, max_digits=10) """


""" class Term(models.Model):
    term = models.CharField(choices=TERM, max_length=10)
    current_term = models.BooleanField(default=False, blank=True, null=True)
    term_start = models.DateField(null=True, blank=True)
    term_end = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.term
 """

""" class RepeatedStudent(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    stage = models.CharField(max_length=100, choices=CLASS)
    term = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        full_name = self.student.first_name + " " + self.student.last_name
        return full_name
 """
