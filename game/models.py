from django.db import models
from django.forms import EmailField
from django.forms import ModelForm

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class Question(models.Model):
    def __str__(self):
        return self.question

    game_mode = models.CharField(max_length=150, default='elmc')
    question = models.CharField(max_length=650, default='')
    answer_1_right_one = models.CharField(max_length=400, default='')
    answer_2 = models.CharField(max_length=400, default='')
    answer_3 = models.CharField(max_length=400, default='')
    answer_4 = models.CharField(max_length=400, default='')
    answer_4 = models.CharField(max_length=400, default='')


class Player(models.Model):
    def __str__(self):
        return self.username

    user = models.OneToOneField('auth.user', on_delete=models.CASCADE)
    username = models.CharField(max_length=80, default='')
    currentQuestion = models.IntegerField(default=0)


class QuestionStat(models.Model):
    game_mode = models.CharField(max_length=150, default='')
    question = models.ForeignKey('game.question', on_delete=models.CASCADE)
    player = models.ForeignKey('game.player', on_delete=models.CASCADE)
    question_text = models.CharField(max_length=650, default='')
    number_answered_right = models.IntegerField(default=0)
    earned_Badge = models.BooleanField(default=False)

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

class PlayerGame(models.Model):
     def __str__(self):
         return self.game_name
     user = models.ForeignKey('auth.user', on_delete=models.CASCADE, default='')
     game_name = models.CharField(max_length=350, default='')
     question = models.ManyToManyField('game.question')

class PlayerGameForm(ModelForm):
    class Meta:
        model = PlayerGame
        fields = '__all__'
        exclude = ('user', 'question')
        #fields = ['game', 'question', 'answer_1_right_one', 'answer_2', 'answer_3', 'answer_4']
    def validate_data(self):
       data = self.cleaned_data['fields']
       return data
    def __init__(self, *args, **kwargs):
        super(PlayerGameForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class PlayerQuestionsForm(ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
        exclude = ('game_mode',)
        #fields = ['game', 'question', 'answer_1_right_one', 'answer_2', 'answer_3', 'answer_4']
    def validate_data(self):
       data = self.cleaned_data['fields']
       return data
    def __init__(self, *args, **kwargs):
        super(PlayerQuestionsForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class UpdateUserForm(ModelForm):
    class Meta:
        model = User
        fields = ("username", "password", "email")
        username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
        email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
        password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    # def save(self, commit=True):
    #     user = super(UserCreationForm, self).save(commit=False)
    #     user.username = self.cleaned_data["username"]
    #     user.password = make_password(self.cleaned_data["password1"],None, 'pbkdf2_sha256')
    #     if commit:
    #         user.save()
    #     return user


class GameModeStat(object):
    theme = ""
    questions = 0
    badges = 0
    status = 0
    social_media = ""
