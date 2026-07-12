from django.urls import path
from .views import TopicListAPIView

app_name = 'api'

urlpatterns = [
    path('topics/', TopicListAPIView.as_view(), name='api_topic_list'),
]