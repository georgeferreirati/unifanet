from django.urls import path
from . import views

app_name = 'solicitacoes'

urlpatterns = [
    path('pdf/', views.generate_pdf, name="pdf"),
    path('', views.home, name="home"),
    path('matricula/', views.matricula, name="matricula"),
    path('matricularaluno/', views.matricular_aluno, name="matricular_aluno"),
    path('boletim/<int:id>/', views.boletim, name="boletim"),
    path('solicitarboletim/', views.solicitar_boletim, name="solicitar_boletim"),
    path('submeterprova/', views.submeter_provas, name="submeter_prova"),
    path('listarprovas/', views.listar_provas, name="listar_provas"),
]