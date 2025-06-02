from django.urls import path
from .views import (HomeView, FlagSubmitView, LeaderBoardView,
                    ScoreView, CtfView, WebView, CryptoView,
                    NetworkView, ReverseEngView)

app_name = "desk"

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('score/', ScoreView.as_view(), name='score'),
    path('submit-flag/', FlagSubmitView.as_view(), name='submit_flag'),
    path('leaderboard/', LeaderBoardView.as_view(), name='leaderboard'),
    path('ctf/', CtfView.as_view(), name='ctf'),
    path('ctf/web', WebView.as_view(), name='webb'),
    path('ctf/crypto', CryptoView.as_view(), name='cryptoo'),
    path('ctf/network', NetworkView.as_view(), name='netww'),
    path('ctf/reveng', ReverseEngView.as_view(), name='reveseng'),
    
]
