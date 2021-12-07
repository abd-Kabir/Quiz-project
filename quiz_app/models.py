from django.contrib.auth.models import User
from django.db import models

from language_app.utils import choices as lang_choices
# Create your models here.
from quiz_4.models import Auditable
from quiz_app.utils import level_choices, category_choices


class Category(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100, unique=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.code = self.name.upper().replace(" ", "_")
        super().save(force_insert, force_update, using, update_fields)

    class Meta:
        db_table = 'question_category'


class Level(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100, unique=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.code = self.name.upper().replace(" ", "_")
        super().save(force_insert, force_update, using, update_fields)

    class Meta:
        db_table = 'question_level'


class Question(Auditable):
    question = models.CharField(max_length=300)
    category = models.CharField(max_length=100, choices=category_choices())
    level = models.CharField(max_length=100, choices=level_choices())
    lang = models.CharField(max_length=100, choices=lang_choices())
    valid = models.BooleanField(default=False)

    def __str__(self):
        return self.question


class QuestionOptions(Auditable):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=300)
    right = models.BooleanField(default=False)


class Quiz(models.Model):
    category = models.CharField(max_length=50, choices=category_choices())
    level = models.CharField(max_length=50, choices=level_choices())
    lang = models.CharField(max_length=50, choices=lang_choices())
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(null=True, default=None)


class QuizOptions(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, models.CASCADE)
    check = models.BooleanField(default=False)
    before_id = models.BigIntegerField(default=None, null=True)
