from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='game_blog-home'),
    path('gamers/',views.users,name='game_blog-user'),
    path('game/',views.game,name='game_blog-game'),
    path('logout/',views.besselama,name='game_blog-bye'),
    path('register/',views.register,name='registre'),   
]