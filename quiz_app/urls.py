from django.urls import path

from quiz_app.views import HomeView, StartQuiz, ProcessQuiz

app_name = 'quiz'
urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('start/', StartQuiz.as_view(), name='start_quiz'),
    path('process/<int:id>', ProcessQuiz.as_view(), name='process_quiz'),
]
