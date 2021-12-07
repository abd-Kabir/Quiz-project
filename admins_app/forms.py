from django import forms

from language_app.utils import choices as lang_choices
from quiz_app.utils import category_choices, level_choices


class CreateQuestionForm(forms.Form):
    category = forms.CharField(label="Category",
                               widget=forms.Select(attrs={'class': 'form-control'}, choices=category_choices()))
    level = forms.CharField(label="Level",
                            widget=forms.Select(attrs={'class': 'form-control'}, choices=level_choices()))
    lang = forms.CharField(label="Language",
                           widget=forms.Select(attrs={'class': 'form-control'}, choices=lang_choices()))
    question = forms.CharField(label='Question', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))



class CreateQuestionOptionForm(forms.Form):
    option = forms.CharField(label="Option", widget=forms.TextInput(attrs={'class': 'form-control'}))
    right = forms.ChoiceField(label="Right ?", widget=forms.CheckboxInput(), choices=[('yes', "Yes"), ('no', 'No')])


class CreateLevelForm(forms.Form):
    level = forms.CharField(label="Level", widget=forms.TextInput(attrs={'class': 'form-control'}))
