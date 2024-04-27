from . import views
from django.views import View
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from .forms import (
    CustomAuthenticationForm,
    CustomPasswordResetForm,
    CustomPasswordSetForm,
)
from django.urls import path


urlpatterns = [
    path(
        "login/", LoginView.as_view(form_class=CustomAuthenticationForm), name="login"
    ),
    path("logout/", LogoutView.as_view(), name="logout"),
]

urlpatterns += [
    path(
        "password_reset/",
        PasswordResetView.as_view(form_class=CustomPasswordResetForm),
        name="password_reset",
    ),
    path(
        "password_reset/done/",
        PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(form_class=CustomPasswordSetForm),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]


urlpatterns += [
    path("parentcreate/", views.ParentCreateView.as_view(), name="parentcreate"),
]
