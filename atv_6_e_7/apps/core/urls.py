from django.urls import path
from .views import *
urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("disc/<int:pk>", DiscView.as_view(), name="disc")
]