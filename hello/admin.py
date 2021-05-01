from django.contrib import admin

from .models import *

admin.site.register(Users)
admin.site.register(Games)
admin.site.register(Rewards)
admin.site.register(Bets)
admin.site.register(DotaPlayerRanking)