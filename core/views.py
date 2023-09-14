from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse_lazy


class IndexView(TemplateView):
    template_name = "index.html"
    success_url = reverse_lazy("index")
