from django.urls import path
from .views import ProcessPromptView, ai_frontend

urlpatterns = [
    path('generate/', ProcessPromptView.as_view(), name='generate'),
    path('frontend/', ai_frontend, name='ai_frontend'),
]