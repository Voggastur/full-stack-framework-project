from django import forms
from .models import Question, Answer


class QuestionForm(forms.ModelForm):
    """ Question form used to populate database from user input """
    class Meta:
        model = Question
        fields = ('text',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update(
            {'rows': 4, 'class': 'form-control mb-4', 'autofocus': True})


class AnswerForm(forms.ModelForm):
    """ Answer form used to recieve admin input """
    class Meta:
        model = Answer
        fields = ('text',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update(
            {'rows': 4, 'class': 'form-control mb-4', 'autofocus': True})
