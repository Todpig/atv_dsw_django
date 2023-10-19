from django.views.generic import TemplateView, DetailView
from .models import *
class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["discs"] = Discs.objects.all()
        return context
    

class DiscView(DetailView):
    model = Discs
    template_name = "disc.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context