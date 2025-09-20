from django.urls import path
from . import views

urlpatterns = [
    path('healthz', views.healthz),
    path('readyz', views.readyz),

    path('auth/register', views.auth_register),
    path('auth/login', views.auth_login),
    path('auth/refresh', views.auth_refresh),
    path('auth/logout', views.auth_logout),
    path('auth/session', views.auth_session),

    path('auth/oauth/<str:provider>', views.auth_oauth_start),
    path('auth/oauth/<str:provider>/callback', views.auth_oauth_callback),

    path('auth/mfa/webauthn/begin', views.webauthn_begin),
    path('auth/mfa/webauthn/finish', views.webauthn_finish),

    path('auth/magic-link', views.magic_link),
    path('auth/magic-link/consume', views.magic_link_consume),

    path('auth/oidc/.well-known/jwks.json', views.jwks),
]
