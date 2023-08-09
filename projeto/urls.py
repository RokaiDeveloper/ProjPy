"""projeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from app.views import home, painel, dologin, dashboard, logouts, create, store, map, perfil, newmap
urlpatterns = [
    path("__debug__/", include("debug_toolbar.urls")),
    path('admin/', admin.site.urls),
    path('', home),
    path('newmap/', newmap),
    path('home/', home),
    path('painel/', painel),
    path('dologin/', dologin),
    path('dashboard/', dashboard),
    path('logouts/', logouts),
    path('map/', map),
    path('perfil/', perfil),
    path('create/', create),
    path('store/', store),
    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name="ResetPassword/resetpass.html"),
         name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="ResetPassword/resetpasssent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="ResetPassword/password_reset_confirm.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="ResetPassword/pass_reset_complete.html"), name="password_reset_complete"),
]