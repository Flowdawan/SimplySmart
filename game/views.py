from django.shortcuts import render

from game.models import Question

# Create your views here.

def signup(request):
    return render(request, 'auth/signup.html')

def signin(request):
    return render(request, 'auth/signin.html')

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