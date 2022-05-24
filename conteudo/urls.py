from django.urls import path
from .views import HomeView, PostagemView, AdicionarPostView, AtualizarPostView, DeletePostView, CategoriaView, PostSearchView, CategoriaListView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('conteudo/<int:pk>/', PostagemView.as_view(), name="post-detail"),
    path('conteudo/adicionar/', AdicionarPostView.as_view(), name="post-add"),
    path('conteudo/editar/<int:pk>/', AtualizarPostView.as_view(), name="update_post"),
    path('conteudo/<int:pk>/remover/',DeletePostView.as_view(), name="delete_post"),
    path('categoria/<str:cats>/', CategoriaView, name="categoria"),
    path('categorias/', CategoriaListView, name="categoria-list"),
    path('pesquisar/', PostSearchView, name="post-search"),
]