from django.views.generic import TemplateView, DetailView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.http import  JsonResponse
from django.views.generic.edit import CreateView
from django.urls import reverse
from django.shortcuts import render
from .forms import DiscsForm
from .models import *
 
class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["discs"] = Discs.objects.all()
        return context
    

def lista_todos_discos(request):
    discs = Discs.objects.all()
    return render(request, 'lista_discos.html', {'discs': discs})

class DiscView(DetailView):
    model = Discs
    template_name = "disc.html"

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        return HttpResponseRedirect(reverse('todos_discos'))
    
class CadastrarDiscoView(CreateView):
    model = Discs
    form_class = DiscsForm
    template_name = 'cadastro_disco.html'

    def get_success_url(self):
        return reverse('disc', args=[self.object.pk])
    
class VisualizarDiscoView(DetailView):
    model = Discs
    template_name = "visualizar_disco.html"

class EditarDiscoView(UpdateView):
    model = Discs
    form_class = DiscsForm
    template_name = "editar_disco.html"
    success_url = '/todos-discos/'

class ConfirmarExclusaoDiscoView(DetailView):
    model = Discs
    template_name = "confirmar_exclusao_disco.html"
    success_url = '/todos-discos/'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return JsonResponse({'message': 'Disco excluído com sucesso'})

class ExcluirDiscoView(DeleteView):
    model = Discs
    success_url = '/todos-discos/'
