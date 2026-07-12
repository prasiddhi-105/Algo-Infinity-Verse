from django.shortcuts import render, get_object_or_404
from .models import Module, Topic

def module_list(request):
    modules = Module.objects.prefetch_related('topics').all()
    return render(request, 'hub/module_list.html', {'modules': modules})

def topic_detail(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    # Fetch all other topics in the same module to display a sidebar navigation layout
    sidebar_topics = topic.module.topics.all()
    # Fetch quizzes associated with this specific topic
    quizzes = topic.quizzes.all()
    
    context = {
        'topic': topic,
        'sidebar_topics': sidebar_topics,
        'quizzes': quizzes,
    }
    return render(request, 'hub/topic_detail.html', context)