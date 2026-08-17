from django.urls import path
from .views import home, about, contact, gallery, items

urlpatterns = [
    path("", home),
    path("about/", about),
    path("contact/", contact),
    path("gallery/", gallery),
    path("items/", items),
]