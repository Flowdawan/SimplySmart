from django import template
register = template.Library()
from game.models import PlayerGameForm
from game.models import PlayerQuestionsForm
from game.models import PlayerGame


from game.models import Question
from game.models import MyRegistrationForm
from game.models import Player
from game.models import QuestionStat


@register.simple_tag
def getCustomGames(request):
    currentUser = request.user.id
    games = PlayerGame.objects.all().filter(user=currentUser)
    return games
