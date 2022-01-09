from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password


from game.models import Question
from game.models import MyRegistrationForm

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, ("Registration Successfull!"))
            return redirect('menu')
    else:
        form = MyRegistrationForm()
    return render(request, 'auth/signup.html', {'form': form})

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('menu')
        else:
            messages.success(request, ("Wrong Credentials, Please Try Again."))
            return redirect('signin')
    else:
        return render(request, 'auth/signin.html')

def signout(request):
    logout(request)
    messages.success(request, ("Successfully logged out"))
    return redirect('signin')

def menu(request):
    return render(request, 'game/menu.html')

def regular_game(request, question_id=0):
    questions = Question.objects.all()
    if question_id >= len(questions):
        question_id = 0
    question = questions[question_id]
    return render(request, 'game/question.html', {'question': question })

def check_answer(request, question_id=0, answer_id=0):
    questions = Question.objects.all()
    question = questions[question_id-1]
    if(answer_id):
        return render(request, 'game/rightAnswer.html', {'question': question, 'id': question_id})
    else:
        return render(request, 'game/wrongAnswer.html', {'question': question, 'id': question_id })