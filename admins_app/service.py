from django.contrib.auth.models import User

from admins_app.forms import CreateQuestionForm, CreateQuestionOptionForm, CreateLevelForm
from quiz_app.models import Question, QuestionOptions, Level


def create_question(form: CreateQuestionForm, user: User) -> Question:
    data = form.cleaned_data
    question = Question()
    question.question = data.get('question')
    question.category = data.get('category')
    question.level = data.get('level')
    question.lang = data.get('lang')
    question.created_by = user
    question.save()
    return question


def create_option(form: CreateQuestionOptionForm, question_id: int, user):
    data = form.data
    right = True if form.data.get('right') else False
    option = QuestionOptions(question_id=question_id, answer=data.get('option'), right=right, created_by=user)
    option.save()


def create_level(form: CreateLevelForm):
    level: str = form.data.get('level')
    Level(name=level, code=level.upper()).save()
