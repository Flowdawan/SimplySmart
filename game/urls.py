from django.urls import path

from . import views

urlpatterns = [
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('signup', views.signup, name='signup'),
    path('menu', views.menu, name='menu'),
    #path('game/specialMode', views.specialMode, name='specialMode'),
    path('regularGame', views.regular_game, name='regularGame'),
    path('regularGame/<int:question_id>', views.regular_game, name='regularGame'),
    path('checkAnswer/<int:question_id>/<str:answer>', views.check_answer, name='checkAnswer'),
    path('auth/manage', views.manageUser, name='manageUser'),
    path('game/customGame/create', views.customGame, name='customGame'),
    path('game/customGame/create/questions/<str:game_names>', views.customGameQuestions, name='customGameQuestions'),
    #path('game/customGame/start', views.startCustomGame, name='startCustomGame'),
    path('game/user/statistic', views.gameStatistic, name='gameStatistic'),


]

