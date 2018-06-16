from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup_view, name="signup"),
    path('', views.login_view, name="login"),
    path('', views.logout_view, name="logout"),
    path('estudante/', views.estudante_signup_view, name="estudante"),
    path('professor/', views.professor_signup_view, name="professor"),
    path('coordenador/', views.coordenador_signup_view, name="coordenador"),
]