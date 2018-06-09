from django.urls import path
from django.urls import include, re_path
from django.conf.urls import url
from search_app import views

# Template tagging
app_name = 'search'

urlpatterns = [
    path('', views.page_search, name='page_search'),
]

