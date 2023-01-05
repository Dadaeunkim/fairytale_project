from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path('', views.PostList.as_view()),
    path('0/', views.list_show_0),
    path('1/', views.list_show_1),
    path('2/', views.list_show_2),
    path('3/', views.list_show_3),
    path('4/', views.list_show_4),
    path('5/', views.list_show_5),
    path('6/', views.list_show_6),
    path('7/', views.list_show_7),
    path('8/', views.list_show_8),
    path('9/', views.list_show_9),
    
]