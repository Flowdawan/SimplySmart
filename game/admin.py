from django.contrib import admin
from .models import Question
from .models import Player
from .models import QuestionStat
from .models import PlayerGame


# Register your models here.

admin.site.register(Question)
admin.site.register(Player)
admin.site.register(QuestionStat)
admin.site.register(PlayerGame)