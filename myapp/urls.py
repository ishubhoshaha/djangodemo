from django.urls import path

from . import views

urlpatterns = [
    path("", views.list, name="list"),
    # ex: /person/5/
    path("<int:person_id>/", views.detail, name="detail"),
    path("create/", views.create_person, name="create_person"),
]