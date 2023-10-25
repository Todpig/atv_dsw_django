from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('disc/<int:pk>/', DiscView.as_view(), name='disc'),
    path('cadastrar-disco/', CadastrarDiscoView.as_view(), name='cadastrar_disco'),
    path('todos-discos/', lista_todos_discos, name='todos_discos'),
    path('visualizar-disco/<int:pk>/', VisualizarDiscoView.as_view(), name='visualizar_disco'),
    path('editar-disco/<int:pk>/', EditarDiscoView.as_view(), name='editar_disco'),
    path('confirmar-exclusao-disco/<int:pk>/', ConfirmarExclusaoDiscoView.as_view(), name='confirmar_exclusao_disco'),
    path('excluir-disco/<int:pk>/', ExcluirDiscoView.as_view(), name='excluir_disco'),
]
