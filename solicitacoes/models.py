from django.db import models
from accounts.models import Professor
from turmas.models import Turma

# Create your models here.
class Prova(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    escolha_bimestre = (
        ('1bimestre','1º Bimestre'),
        ('2bimestre', '2º Bimestre'),
        ('3bimestre', '3º Bimestre'),
        ('4bimestre', '4º Bimestre'),
    )
    bimestre = models.CharField(max_length=12, choices=escolha_bimestre)
    arquivo = models.FileField()