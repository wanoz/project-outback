from django.urls import path
from django.urls import include, re_path
from contact_app import views

# Template tagging
app_name = 'contact'

urlpatterns = [
    path('', views.page_feedback, name='page_feedback'),
    path('thanks/', views.page_tyfeedback, name="page_tyfeedback")
]