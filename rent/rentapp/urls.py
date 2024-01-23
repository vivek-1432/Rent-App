from django.contrib import admin
from django.urls import path
from rentapp import views
from rent import settings
from django.conf.urls.static import static

urlpatterns = [
    path('create', views.create),
    path('dashboard', views.dashboard),
    path('delete/<rid>', views.delete),
    path('edit/<rid>', views.edit),
    path('', views.home),
    path('register', views.register),
    path('login', views.user_login),
    path('user_logout', views.user_logout)
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)