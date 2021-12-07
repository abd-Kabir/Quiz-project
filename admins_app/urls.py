from django.urls import path

from admins_app.views import (HomeView,
                              CreateQuestionView,
                              CreateQuestionOptionView,
                              QuestionListView,
                              CreateLevelView, QuizUpdate, QuizDelete)

app_name = 'admins'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create/', CreateQuestionView.as_view(), name='create_question'),
    path('list/', QuestionListView.as_view(), name='question_list'),
    path('add_option/<int:question_id>', CreateQuestionOptionView.as_view(), name='add_option'),
    path('create/level/', CreateLevelView.as_view(), name='create_level'),
    path('quiz-update/<int:pk>/', QuizUpdate.as_view(), name='quiz-update'),
    path('quiz-delete/<int:pk>/', QuizDelete.as_view(), name='quiz-delete'),
]
