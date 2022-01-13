from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from game.models import Question
from game.models import MyRegistrationForm
from game.models import Player
from game.models import QuestionStat


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
    questionstat = getCurrentQuestion(request, question)
    return render(request, 'game/question.html', {'question': question, 'questionstat': questionstat})


def check_answer(request, question_id=0, answer_id=0):
    questions = Question.objects.all()
    question = questions[question_id - 1]
    if (answer_id):
        currentQuestion = getCurrentQuestion(request, question)
        currentQuestion.number_answered_right = currentQuestion.number_answered_right + 1
        currentQuestion.save()
        isEarnedBadge(currentQuestion)
        return render(request, 'game/rightAnswer.html', {'question': question, 'id': question_id})
    else:
        return render(request, 'game/wrongAnswer.html', {'question': question, 'id': question_id})


def getCurrentPlayer(request):
    currentUser = request.user
    result = Player.objects.filter(user=currentUser.id)
    if result.exists():
        return result[0]
    else:
        newObject = Player(user=currentUser, username=currentUser.username, currentQuestion=0)
        newObject.save()
        return newObject

def getCurrentQuestion(request, question):
    currentPlayer = getCurrentPlayer(request)
    pId = currentPlayer.id
    tmp = QuestionStat.objects.filter(player=pId)
    result = tmp.filter(question=question.id)
    if result.exists():
        return result[0]
    else:
        newObject = QuestionStat(question=question, player=currentPlayer, number_answered_right=0)
        newObject.save()
        return newObject


def isEarnedBadge(question):
    if question.number_answered_right == 3:
        question.earned_Badge = True
        question.save()

def manageUser(request):
    return render(request, 'auth/manageUser.html')

def customGame(request):
    return render(request, 'game/customGame/gameCreate.html')