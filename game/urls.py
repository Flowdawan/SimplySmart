from django.urls import path

from . import views

urlpatterns = [
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('signup', views.signup, name='signup'),
    path('menu', views.menu, name='menu'),
    path('emgame', views.regular_game, name='emgame'),
    path('emgame/<int:question_id>', views.regular_game, name='emgame'),
    path('checkAnswer/<int:question_id>/<int:answer_id>', views.check_answer, name='checkAnswer'),
]
