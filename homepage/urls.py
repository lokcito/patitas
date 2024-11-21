from django.urls import path
from . import views
urlpatterns = [
    path("", views.v_index, name="index"),
    path("feedback/create", views.v_feedback_create, name="feedback_create"),
    path("feedback/gracias", views.v_feedback_gracias, name="feedback_gracias")
]