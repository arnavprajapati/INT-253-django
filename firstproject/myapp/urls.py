from django.urls import path
from .views import home, about, contact, gallery, items, students, greet

urlpatterns = [
    path("", home),
    path("about/", about),
    path("contact/", contact),
    path("gallery/", gallery),
    path("items/", items),
    path("students/<int:marks>/", students),
    path("greet/<str:name>/", greet),
]