from django.db import models

class Module(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']

class Topic(models.Model):
    DIFFICULTY_CHOICES = [
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
    ]
    
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='topics')
    title = models.CharField(max_length=200)
    content = models.TextField(help_text="Write the tutorial content here (supports Markdown formatting later).")
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='Medium')
    order = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.module.title} - {self.title}"

    class Meta:
        ordering = ['order']

class QuizQuestion(models.Model):
    OPTION_CHOICES = [
        ('A', 'Option A'),
        ('B', 'Option B'),
        ('C', 'Option C'),
        ('D', 'Option D'),
    ]

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='quizzes')
    question_text = models.CharField(max_length=500)
    option_a = models.CharField(max_length=200)
    option_b = models.CharField(max_length=200)
    option_c = models.CharField(max_length=200)
    option_d = models.CharField(max_length=200)
    correct_option = models.CharField(max_length=1, choices=OPTION_CHOICES)

    def __str__(self):
        return self.question_text