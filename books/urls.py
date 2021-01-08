from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("updatelist", views.update_list, name="updatelist"),
    path("readinglist", views.readinglist_view, name="readinglist")
]