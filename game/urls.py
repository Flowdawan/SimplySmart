from django.urls import path

from . import views

urlpatterns = [
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('menu', views.menu, name='menu'),
    path('emgame', views.regular_game, name='emgame'),
]
