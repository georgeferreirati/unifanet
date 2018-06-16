from django.db import models
from django.contrib.auth.models import Group, User
from django.core.validators import MaxValueValidator, MinValueValidator
from accounts.models import Estudante, Professor, Coodenador

# Create your models here.
# Criando a classe Turma
class Turma(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    estudantes = models.ManyToManyField(Estudante)
    professor = models.ManyToManyField(Professor)
    coordenador = models.ManyToManyField(Coodenador)

    def __str__(self):
        return self.name

    def snippet(self):
        return self.description[:50] + '...'

class Aula(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    presenca = models.ManyToManyField(Estudante)

    def __str__(self):
        return self.title

class Nota(models.Model):
    nota1 = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    nota2 = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    nota3 = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    nota4 = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    aluno = models.ForeignKey(Estudante, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)

    def __str__(self):
        return self.aluno.user.get_full_name()

class Postagem(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Resposta(models.Model):
    postagem = models.ForeignKey(Postagem, on_delete=models.CASCADE)
    texto = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.postagem.titulo
