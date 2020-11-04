from django.urls import path
from faq import views

urlpatterns = [
    path('', views.faq, name='faq'),
    path('add_question', views.add_question, name='add_question'),
    path('edit/<int:question_id>/', views.edit_question, name='edit_question'),
    path('delete/<int:question_id>/', views.delete_question, name='delete_question'),
    path('add_answer/<int:question_id>/', views.add_answer, name='add_answer'),
    path('edit_answer/<int:answer_id>/', views.edit_answer, name='edit_answer'),
    path('delete_answer/<int:answer_id>/', views.delete_answer, name='delete_answer'),
]
