from django.shortcuts import render
from .models import Question, Answer
from .forms import QuestionForm

# Create your views here.


def faq(request):
    """ Returns the Frequently Asked Questions template and
    show the Question Form if user wish to POST """

    questions = Question.objects.all()
    answers = Answer.objects.all()
    qform = QuestionForm()

    context = {
        'questions': questions,
        'answers': answers,
        'qform': qform,
    }

    return render(request, 'faq/faq.html', context)
