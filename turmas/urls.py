from django.urls import path
from . import views

app_name = 'turmas'

urlpatterns = [
    #Lista de Turmas (Caso não digitem nada na URL, abre a tela de Turmas)
    path('', views.turmas_list, name="list"),

    #Toda as URLs do Menu de Turmas
    path('<int:id>', views.turmas_detail, name="detail"),
    path('<int:id>/aulas/', views.turmas_aulas, name="aulas"),
    path('<int:id>/alunos/', views.turmas_alunos, name="alunos"),
    path('<int:id>/notas/', views.turmas_notas, name="notas"),
    path('<int:id>/forum/', views.turmas_forum, name="forum"),

    #Todas as URLs de Cadastro e Atualização de Turma
    path('criarturma/', views.criar_turma, name="criar_turma"),
    path('<int:id>/atualizarturma/', views.atualizar_turma, name="atualizar_turma"),

    #Todas as URLs de Cadastro e Atualização de Aula
    path('<int:id>/aulas/<int:id1>/delete/', views.excluir_aula, name="excluir_aula"),
    path('<int:id>/aulas/<int:id1>/update/', views.atualizar_aula, name="atualizar_aula"),
    path('<int:id>/aulas/criaraula/', views.criar_aula, name="criar_aula"),
    path('<int:id>/aulas/<int:id1>/presenca/', views.presenca_aula, name="presenca"),
    path('<int:id>/notas/criarnota/', views.criar_nota, name="criar_nota"),
    path('<int:id>/alunos/add/', views.add_estudantes, name="add_alunos"),
    path('<int:id>/forum/criarpostagem/', views.criar_postagem, name="criar_postagem"),
    path('<int:id>/forum/<int:id1>/update/', views.atualizar_postagem, name="atualizar_postagem"),
    path('<int:id>/forum/<int:id1>/delete/', views.excluir_postagem, name="excluir_postagem"),
    path('<int:id>/forum/<int:id1>/', views.exibir_postagem, name="exibir_postagem"),
    path('<int:id>/forum/<int:id1>/criarresposta/', views.criar_resposta, name="criar_resposta"),
]