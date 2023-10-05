from django.urls import path

from .views import subject_form, subject_list, subject_edit, teacher_form, teacher_edit

urlpatterns = [
    path("subject", subject_form, name="subject_form"),
    path("subjects", subject_list, name="subject_list"),
    path("subject/<int:pk>", subject_edit, name="subject_edit"),
    path("teacher", teacher_form, name="teacher_form"),
    path("teacher/<int:pk>", teacher_edit, name="teacher_edit"),
]
