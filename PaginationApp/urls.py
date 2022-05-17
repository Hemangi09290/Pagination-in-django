from django.urls import path
from PaginationApp import views

urlpatterns = [
    path("", views.ContactListView.as_view()),
]
