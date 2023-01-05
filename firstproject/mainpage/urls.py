from django.urls import path, include
from .views import *
from . import views

urlpatterns = [
    path('', MainpageView.as_view(), name='mainpage'),
    path('readingpage/', include('readingpage.urls')),
    path('custompage/', views.custom),
    path('custompage1/', views.bookillu_custom),

]