from django.urls import path
from .views import (
        QuestionListView,
        UserQuestionListView,
        QuestionDetailView,
        QuestionCreateView,
        QuestionUpdateView,
        QuestionDeleteView,
        QuestionDetail,
        DeleteResponse,
        )


app_name = 'forum'
urlpatterns = [
    path('', QuestionListView.as_view(), name='list'),
    path('<str:username>/', UserQuestionListView.as_view(), name='user-question'),
    path('question/<int:pk>/', QuestionDetailView.as_view(), name='question-detail'),
    path('question/<int:question_id>/response/', QuestionDetail, name='question-detail-response'),
    path('question/new/', QuestionCreateView.as_view(), name='question-create'),
    path('question/<int:pk>/update/', QuestionUpdateView.as_view(), name='question-update'),
    path('question/<int:pk>/delete/', QuestionDeleteView.as_view(), name='question-delete'),
    path('response/<int:response_id>/delete/', DeleteResponse, name='delete-response'),
    ]
