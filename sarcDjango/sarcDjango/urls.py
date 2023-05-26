from django.urls import path
from . import views

urlpatterns = [
    path('crud-form/', views.crud_form, name='crud_form'),
    path('feedback-form/', views.feedback_form, name='feedback_form'),
    # Add other URLs as needed
]
