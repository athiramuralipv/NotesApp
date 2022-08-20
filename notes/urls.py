from django.urls import path
from notes import views

urlpatterns=[
    path("accounts/signup", views.SignUpView.as_view(), name="signup"),
    path("accounts/login", views.LogInView.as_view(), name="signin"),
    path("home",views.CreateNotesView.as_view(),name="home"),
    path("user/notes",views.ViewMyNotes.as_view(),name="view-notes")
]