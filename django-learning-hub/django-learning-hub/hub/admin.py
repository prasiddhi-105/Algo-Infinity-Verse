from django.contrib import admin
from .models import Module, Topic, QuizQuestion

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    search_fields = ('title',)

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'module', 'difficulty', 'order')
    list_filter = ('difficulty', 'module')
    search_fields = ('title', 'content')

@admin.register(QuizQuestion)
class QuizQuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'topic', 'correct_option')
    list_filter = ('topic',)
    search_fields = ('question_text',)