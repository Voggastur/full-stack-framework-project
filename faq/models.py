from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    """ ForeignKey has SET_NULL on delete so that
    the Question remains if User is deleted """

    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name="faq_questions")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    text = models.TextField(
        max_length=1000, default="Question details")

    def __str__(self):
        return self.text


class Answer(models.Model):
    """ OneToOneField is used to limit one answer per question,
    and on_delete=Cascade ensures answer deletion on question deletion """

    related_question = models.OneToOneField(
        Question, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    text = models.TextField(max_length=1000)

    def __str__(self):
        return self.text
