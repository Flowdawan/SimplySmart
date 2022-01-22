from random import randint
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse

from game.models import PlayerGameForm
from game.models import PlayerQuestionsForm
from game.models import PlayerGame
from game.models import UpdateUserForm

from game.models import Question
from game.models import MyRegistrationForm
from game.models import Player
from game.models import QuestionStat
from game.models import GameModeStat

from game.templatetags import htmlEscape


def specialMode(request):
    return redirect('https://simplysmart.at/')


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


def regular_game(request, question_id=0, gameMode='elmc'):
    questions = Question.objects.all().filter(game_mode=gameMode)
    if question_id >= len(questions):
        question_id = 0
    question = questions[question_id]
    if request.user.is_authenticated:
        questionstat = getCurrentQuestion(request, question)
    else:
        questionstat = ''
    answers = []
    answers.append(htmlEscape.htmlspecialchars(question.answer_1_right_one))
    answers.append(htmlEscape.htmlspecialchars(question.answer_2))
    answers.append(htmlEscape.htmlspecialchars(question.answer_3))
    answers.append(htmlEscape.htmlspecialchars(question.answer_4))
    return render(request, 'game/question.html',
                  {'question': question, 'id': question_id, 'questionstat': questionstat, 'answers': answers,
                   'gameMode': gameMode})


def game_statistic(request):
    if request.user.is_authenticated:
        currentuser = getCurrentPlayer(request)
        answeredquestions = QuestionStat.objects.all().filter(player=currentuser)
        gamemodes = []
        gamemodesstats = []
        for x in answeredquestions:
            if x.game_mode not in gamemodes:
                stat = GameModeStat()
                stat.theme = x.game_mode
                stat.questions = len(Question.objects.all().filter(game_mode=x.game_mode))
                stat.badges = len(QuestionStat.objects.all().filter(earned_Badge=True, game_mode=x.game_mode, player=currentuser))
                rightquestions = len(QuestionStat.objects.all().filter(number_answered_right__gte=1, game_mode=x.game_mode, player=currentuser))
                try:
                    stat.status = round((rightquestions/stat.questions) * 100, 2)
                except ZeroDivisionError:
                    stat.status = 0
                stat.social_media = "Look! I have completed " + str(stat.status) + "% of the " + stat.theme + \
                                    "-Quiz and earned " + str(stat.badges) + " Badges!\nCheck it out on: "
                gamemodes.append(x.game_mode)
                gamemodesstats.append(stat)
        return render(request, 'game/gameStatistic.html', {'gamemodesstats': gamemodesstats})
    else:
        return redirect('signin')


def check_answer(request, question_id=0, answer='', gameMode='elmc'):
    questions = Question.objects.all().filter(game_mode=gameMode)
    question = questions[question_id]
    question_id += 1
    if (answer == htmlEscape.htmlspecialchars(question.answer_1_right_one)):
        if request.user.is_authenticated:
            currentQuestion = getCurrentQuestion(request, question)
            currentQuestion.number_answered_right = currentQuestion.number_answered_right + 1
            currentQuestion.save()
            isEarnedBadge(currentQuestion)
        return render(request, 'game/rightAnswer.html', {'question': question, 'id': question_id, 'gameMode': gameMode})
    else:
        return render(request, 'game/wrongAnswer.html', {'question': question, 'id': question_id, 'gameMode': gameMode})


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
        newObject = QuestionStat(question=question, player=currentPlayer, number_answered_right=0, game_mode=question.game_mode)
        newObject.save()
        return newObject


def isEarnedBadge(question):
    if question.number_answered_right == 3:
        question.earned_Badge = True
        question.save()


def manageUser(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = UpdateUserForm(request.POST, instance=request.user)
            if form.is_valid():
                password = request.POST['password']
                user = form.save()
                user.set_password(password)
                user.save()
                messages.success(request, 'Your profile is updated successfully')
                return redirect('menu')
        else:
            form = UpdateUserForm()
            return render(request, 'auth/manageUser.html', {'form': form})
        return render(request, 'menu')
    else:
        return redirect('signin')


def customGame(request):
    if request.user.is_authenticated:
        # if this is a POST request we need to process the form data
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = PlayerGameForm(request.POST)
            # check whether it's valid:
            if form.is_valid():
                # process the data in form.cleaned_data as required
                newGame = form.save(commit=False)
                newGame.user = request.user
                newGame.save()
                if request.POST.get("next"):
                    game_names = request.POST.get("game_name")
                    # return redirect('menu')
                    form = PlayerQuestionsForm()
                    url = reverse('customGameQuestions', args=(game_names,))
                    return HttpResponseRedirect(url)
                else:
                    return redirect('menu')
            else:
                return HttpResponseRedirect('')

        # if a GET (or any other method) we'll create a blank form
        else:
            form = PlayerGameForm()
            return render(request, 'game/customGame/gameCreate.html', {'form': form})
    else:
        return redirect('signin')


def customGameQuestions(request, game_names):
    game = PlayerGame.objects.get(game_name=game_names)
    print(game)
    if request.user.is_authenticated:
        # if this is a POST request we need to process the form data
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = PlayerQuestionsForm(request.POST)
            # check whether it's valid:            
            if form.is_valid():
                # process the data in form.cleaned_data as required
                newQuestion = form.save(commit=False)
                newQuestion.game_mode = game
                newQuestion.save()
                if request.POST.get("next"):
                    return HttpResponseRedirect('')
                else:
                    return redirect('menu')
            else:
                print()
                return redirect('menu')

        # if a GET (or any other method) we'll create a blank form
        else:
            form = PlayerQuestionsForm()
            return render(request, 'game/customGame/questions.html', {'form': form, 'game_names': game_names})
    else:
        return redirect('signin')