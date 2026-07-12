from rest_framework import serializers
from hub.models import Topic, QuizQuestion

class QuizQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizQuestion
        fields = ['id', 'question_text', 'option_a', 'option_b', 'option_c', 'option_d']

class TopicAPISerializer(serializers.ModelSerializer):
    quizzes = QuizQuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Topic
        fields = ['id', 'title', 'content', 'difficulty', 'quizzes']