from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from profiles.models import UserProfile
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm

# Create your views here.


def faq(request):
    """ Returns the Frequently Asked Questions template and
    show the Question Form if user wish to POST """

    questions = Question.objects.all()
    answers = Answer.objects.all()

    context = {
        'questions': questions,
        'answers': answers,
    }

    return render(request, 'faq/faq.html', context)


@login_required
def add_question(request):

    user = get_object_or_404(UserProfile, user=request.user)
    qform = QuestionForm()

    if request.method == 'POST':

        qform = QuestionForm(request.POST)
        form_input = {
            'text': request.POST['text']
            }
        qform = QuestionForm(form_input)

        if qform.is_valid():
            question = qform.save(commit=False)
            question.created_by = request.user
            question.save()
            messages.success(request,
                             f'Thank you {user}, your question has been posted!')
        else:
            messages.error(request,
                           'Sorry, an error has occured when posting your question, please try again!')
        return redirect('faq')

    return render(request, 'faq/add_question.html', {"qform": qform})


@login_required
def edit_question(request, question_id):
    """ View to edit existing question, and handle post of edited question """

    question = get_object_or_404(Question, pk=question_id)
    user = get_object_or_404(UserProfile, user=request.user)
    qform = QuestionForm(instance=question)

    if request.method == "POST":
        qform = QuestionForm(request.POST, instance=question)
        if qform.is_valid():
            qform.save()
            messages.success(request,
                             f'Thank you {user}, Question has been updated!')
            return redirect(reverse('faq'))
        else:
            messages.error(request,
                           'An error has occured when updating the question, please try again')

    template = 'faq/edit_question.html'
    context = {
        'question': question,
        'qform': qform,
    }
    return render(request, template, context)


@login_required
def delete_question(request, question_id):
    """ Delete a question """

    question = get_object_or_404(Question, id=question_id)
    question.delete()
    messages.success(request, 'Question has been deleted.')

    return redirect('faq')


@login_required
def add_answer(request, question_id):
    """ Handle POST data to add answer next to questions on faq page,
    else show the add review form in preparation of POST """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    user = get_object_or_404(UserProfile, user=request.user)
    question = get_object_or_404(Question, pk=question_id)
    answer_form = AnswerForm()

    if request.method == 'POST':
        answer_form = AnswerForm(request.POST, instance=question)
        form_input = {
            'text': request.POST['text']
            }
        answer_form = AnswerForm(form_input)

        if answer_form.is_valid():
            answer = answer_form.save(commit=False)
            answer.related_question = question
            question.related_answer = answer
            answer.save()
            question.save()
            messages.success(request,
                             'Answer has been posted!')
        else:
            messages.error(request,
                           'Sorry, an error has occured when posting your answer, please try again!')
        return redirect('faq')
    else:
        answer_form = AnswerForm()

    context = {
        "question": question,
        "answer_form": answer_form,
    }

    return render(request, 'faq/add_answer.html', context)


@login_required
def edit_answer(request, answer_id):
    """ View to edit an existing answer """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    answer = get_object_or_404(Answer, pk=answer_id)
    answer_form = AnswerForm(instance=answer)
    user = get_object_or_404(User, username=request.user)

    if request.method == "POST":
        answer_form = AnswerForm(request.POST, instance=user)
        if answer_form.is_valid():
            answer_form.save()
            messages.success(request,
                             'Answer has been updated!')
            return redirect('faq')

        else:
            messages.error(request,
                           'An error has occured when updating the answer, please try again')

    template = 'faq/edit_answer.html'
    context = {
        'answer': answer,
        'answer_form': answer_form,
    }
    return render(request, template, context)


@login_required
def delete_answer(request, answer_id):
    """ Delete an answer """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    answer = get_object_or_404(Answer, pk=answer_id)
    answer.delete()
    messages.success(request, 'Answer has been deleted.')

    return redirect('faq')
