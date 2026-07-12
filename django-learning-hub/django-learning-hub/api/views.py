from rest_framework.generics import ListAPIView
from hub.models import Topic
from .serializers import TopicAPISerializer

class TopicListAPIView(ListAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicAPISerializer