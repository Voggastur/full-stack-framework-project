from django.db import models
from django.contrib.auth.models import User


class Answer(models.Model):
    """ Model for Answer """

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    text = models.TextField(max_length=1000)
    related_question = models.ForeignKey('Question', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Question(models.Model):
    """ OneToOneField is used to limit one answer per question,
    User has SET_NULL on delete so that
    the Question remains if User is deleted """

    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name="faq_questions")
    related_answer = models.OneToOneField(
        Answer, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    text = models.TextField(
        max_length=1000, default="Question details")

    def __str__(self):
        return self.text
