from django.db import models
from django.forms import EmailField

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class Question(models.Model):
    def __str__(self):
        return self.question_1

    question_1 = models.CharField(max_length=650, default='')
    answer_1_right_one = models.CharField(max_length=400, default='')
    answer_2 = models.CharField(max_length=400, default='')
    answer_3 = models.CharField(max_length=400, default='')
    answer_4 = models.CharField(max_length=400, default='')
    answer_4 = models.CharField(max_length=400, default='')


class MyRegistrationForm(UserCreationForm):
    email = EmailField(label="Email address", required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.username = self.cleaned_data["username"]
        user.email_address = self.cleaned_data["email"]
        user.password = make_password(self.cleaned_data["password1"], None, 'pbkdf2_sha256')
        if commit:
            user.save()
        return user
