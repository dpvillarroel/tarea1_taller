from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('breaking/', views.breaking, name='breaking'),
    path('saul/', views.saul, name='saul'),
    path('season/<int:pk>', views.season, name='home-season'),
    path('seasonbad/<int:pk>', views.seasonbad, name='home-season-bad'),
    path('episode/<int:pk>', views.episode, name='episode'),
    path('character/<str:pk>', views.character, name='character'),
    path('search/', views.search, name='search'),

]
