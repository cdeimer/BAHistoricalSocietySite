from django.urls import path
from bahs import views

urlpatterns = [
    path("", views.home, name="home"),
    path("history/<int:page_id>/", views.page_detail, name="page_detail")
]