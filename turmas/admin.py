from django.contrib import admin

# Register your models here.
from .models import Turma, Aula, Nota, Postagem, Resposta

admin.site.register(Turma) # Registrando a classe Turma no BD
admin.site.register(Aula)
admin.site.register(Nota)
admin.site.register(Postagem)
admin.site.register(Resposta)