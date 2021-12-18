from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from basic_app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.IndexView.as_view(), name="index"),
    path("basic_app/", include("basic_app.urls", namespace="basic_app")),
]
