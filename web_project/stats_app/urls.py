from django.urls import path
from django.urls import include, re_path
from stats_app import views

app_name = 'stats'

urlpatterns = [
    path('', views.page_stats, name='page_stats'),
]