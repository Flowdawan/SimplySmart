from django.shortcuts import render

# Create your views here.


def signup(request):
    return render(request, 'auth/signup.html')


def signin(request):
    return render(request, 'auth/signin.html')

def menu(request):
    return render(request, 'game/menu.html')

def regular_game(request):
    return render(request, 'game/question.html')
