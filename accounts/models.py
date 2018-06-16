from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_estudante = models.BooleanField(default=False)
    is_professor = models.BooleanField(default=False)
    is_coordenador = models.BooleanField(default=False)
    is_administrador = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Estudante(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    matricula = models.IntegerField(null=True, blank=True)
    nome_mae = models.CharField(max_length=100, null=True, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)
    ano_ingresso = models.IntegerField(null=True, blank=True)
    serie = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.user.get_full_name()

class Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.IntegerField(null=True, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)
    telefone = models.IntegerField(null=True, blank=True)
    endereco = models.CharField(max_length=100, null=True, blank=True)
    formacao = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.user.get_full_name()

class Coodenador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.IntegerField(null=True, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)
    telefone = models.IntegerField(null=True, blank=True)
    endereco = models.CharField(max_length=100, null=True, blank=True)
    formacao = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.user.get_full_name()