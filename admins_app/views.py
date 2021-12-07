from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, DeleteView

from admins_app.forms import CreateQuestionForm, CreateQuestionOptionForm, CreateLevelForm
from admins_app.service import create_question, create_option, create_level
# Create your views here.
from language_app.models import Language
from language_app.utils import choices as lang_choices
from quiz_app.models import Question, Category, Level, QuestionOptions
from quiz_app.utils import level_choices, category_choices


# Commit by Javohir

class HomeView(TemplateView):
    template_name = 'admins_home.html'


class CreateQuestionView(TemplateView):
    template_name = 'question/create_question.html'

    def get(self, request, *args, **kwargs):
        values = {
            "level": level_choices(),
            "category": category_choices(),
            "lang": lang_choices(),
        }
        form = CreateQuestionForm(data=values)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = CreateQuestionForm(request.POST)
        if form.is_valid():
            question = create_question(form, request.user)
            return redirect('admins:add_option', question.id)
        return render(request, self.template_name, {'form': form})


class CreateQuestionOptionView(TemplateView):
    template_name = 'option/add_option.html'

    def get(self, request, *args, **kwargs):
        form = CreateQuestionOptionForm()
        question = Question.objects.get(pk=int(kwargs['question_id']))
        options = QuestionOptions.objects.filter(question=question)
        return render(request, self.template_name, {'form': form, 'question': question, 'options': options})

    def post(self, request, *args, **kwargs):
        form = CreateQuestionOptionForm(request.POST)
        create_option(form, kwargs['question_id'], request.user)
        return redirect("admins:add_option", kwargs['question_id'])


class QuestionListView(ListView):
    model = Question
    context_object_name = 'questions'
    template_name = 'question/question_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        page_number = self.request.GET.get('page', 1)
        category_filter = self.request.GET.get('category_filter')
        level_filter = self.request.GET.get('level_filter')
        lang_filter = self.request.GET.get('lang_filter')
        search = self.request.GET.get('search')

        context = super().get_context_data(object_list=object_list, **kwargs)
        questions = self.model.objects.filter(
            Q(question__contains=(search or '')) &
            Q(category__startswith=(category_filter or '')) &
            Q(level__startswith=(level_filter or '')) &
            Q(lang__startswith=(lang_filter or ''))
        ).all()
        paginator = Paginator(questions, 5)
        page_obj = paginator.get_page(page_number)
        context['questions'] = page_obj
        context['categories'] = Category.objects.all()
        context['levels'] = Level.objects.all()
        context['langs'] = Language.objects.all()
        context['total'] = questions.count()

        return context


class CreateLevelView(TemplateView):
    template_name = 'level/create_level.html'

    def get(self, request, *args, **kwargs):
        form = CreateLevelForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = CreateLevelForm(request.POST)
        create_level(form)
        return redirect("admins:home")


class QuizUpdate(LoginRequiredMixin, UpdateView):
    model = Question
    fields = ['level', 'category', 'lang','question']
    template_name = 'question/update_questions.html'
    success_url = reverse_lazy('admins:question_list')
    # form_class = CreateQuestionForm


class QuizDelete(LoginRequiredMixin, DeleteView):
    model = Question
    context_object_name = 'question'
    template_name = 'question/question_confirm_delete.html'
    success_url = reverse_lazy('admins:question_list')
