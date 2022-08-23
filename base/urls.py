from django.urls import path
from base import views

urlpatterns = [
    path("", views.index, name="index"),
    path("save-student", views.save_student, name="save-student"),
    path("delete-student", views.delete_student, name="delete-student"),
    path("edit-student", views.edit_student, name="edit-student"),
]