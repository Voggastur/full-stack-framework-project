from django.contrib import admin
from .models import Question, Answer

# Register your models here.


class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'text',
        'created_at',
        'created_by',
    )


class AnswerAdmin(admin.ModelAdmin):
    list_display = (
        'text',
        'created_at',
        'related_question',
    )


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
