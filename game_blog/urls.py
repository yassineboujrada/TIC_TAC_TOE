from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='game_blog-home'),
    path('game/',views.game,name='game_blog-game'),
]