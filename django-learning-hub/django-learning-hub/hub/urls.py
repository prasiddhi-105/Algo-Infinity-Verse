from django.urls import path
from . import views

app_name = 'hub'

urlpatterns = [
    path('', views.module_list, name='module_list'),
    path('topic/<int:topic_id>/', views.topic_detail, name='topic_detail'),
]