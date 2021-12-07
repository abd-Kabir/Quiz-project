from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

# Create your views here.
from language_app.models import Language
from quiz_app.models import Category, Question, Level, Quiz, QuizOptions, QuestionOptions


class HomeView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        context = []
        categories = Category.objects.all()
        for category in categories:
            category_code = category.code
            count = Question.objects.filter(category=category_code).count()
            data = {
                "name": category.name,
                "code": category.code,
                "count": count,
            }
            context.append(data)
        return render(request, self.template_name, {
            'context': context,
            'categories': categories,
            'levels': Level.objects.all(),
            'langs': Language.objects.all()
        })


class StartQuiz(TemplateView):
    template_name = 'quiz.html'

    def _allowed_methods(self):
        return ['POST', ]

    def post(self, request, *args, **kwargs):
        lang: str = request.POST.get('lang')
        category: str = request.POST.get('category')
        level: str = request.POST.get('level')
        count: int = int(request.POST.get('count'))
        quiz = Quiz.objects.filter(Q(created_by=request.user) & Q(finished_at=None)).first()
        if not quiz:
            questions = Question.objects.filter(
                Q(category__startswith=(category or '')) &
                Q(level__startswith=(level or '')) &
                Q(lang__startswith=(lang or ''))
            ).all()[:count]

            quiz = Quiz(category=category, level=level, lang=lang, created_by=request.user)
            quiz.save()
            before_id = None
            for question in questions:
                qo = QuizOptions(question=question, quiz=quiz, before_id=before_id)
                qo.save()
                before_id = qo.id
        else:
            messages.error(request, "You Already have Non Completed Quiz please complete it ?")
        quiz_option = QuizOptions.objects.filter(Q(quiz=quiz)).order_by("id").first()
        return redirect('quiz:process_quiz', quiz_option.id)


class ProcessQuiz(TemplateView):
    template_name = 'process_quiz.html'

    def get(self, request, *args, **kwargs):
        quiz_option_id: int = int(kwargs['id'])
        qo = QuizOptions.objects.filter(before_id=quiz_option_id)
        question_id = qo.question_id
        options = QuestionOptions.objects.filter(question_id=question_id).all()
        return render(request, self.template_name, {
            'question': qo.question.question,
            'next_id': 12,
            'options': options
        })

    def post(self, request, *args, **kwargs):
        pass
