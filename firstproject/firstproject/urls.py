from django.contrib import admin
from django.urls import path, include
from .views import home

urlpatterns = [
    path("", include("myapp.urls")),
    path("", home),
    path("admin/", admin.site.urls),
]