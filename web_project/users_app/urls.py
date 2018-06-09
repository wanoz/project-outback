from django.urls import path
from django.urls import include, re_path
from users_app import views

app_name = 'users'

urlpatterns = [
    path('login', views.page_login, name='page_login'),
    path('register', views.page_register, name='page_register'),
    path('logout', views.user_logout, name='logout'),
    path('login/thanks', views.page_tylogin, name='page_tylogin')
]