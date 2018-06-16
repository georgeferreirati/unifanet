from django.shortcuts import render, redirect
from .models import Turma, Aula, Nota, Postagem, Resposta
from .forms import TurmaForm, AulaForm, PresencaForm, NotaForm, AddEstudantesForm, PostagemForm, RespostaForm
from django.forms.models import modelformset_factory
from django.contrib.auth.decorators import login_required

# Renderiza um HTML com uma lista de todas as Turmas
@login_required(login_url="/")
def turmas_list(request):
    turmas = Turma.objects.all().order_by('-name')
    return render(request, 'turmas/turmas_list.html', {'turmas': turmas})

#Todas as Views do Menu de Turma
@login_required(login_url="/")
def turmas_detail(request, id):
    turma = Turma.objects.get(id=id)
    return render(request, 'turmas/turma_detail.html', {'turma': turma})

@login_required(login_url="/")
def turmas_aulas(request, id):
    turma = Turma.objects.get(id=id)
    return render(request, 'turmas/turma_aulas.html', {'turma': turma})

@login_required(login_url="/")
def turmas_alunos(request, id):
    turma = Turma.objects.get(id=id)
    return render(request, 'turmas/turma_alunos.html', {'turma': turma})

@login_required(login_url="/")
def turmas_notas(request, id):
    turma = Turma.objects.get(id=id)
    return render(request, 'turmas/turma_notas.html', {'turma': turma})

@login_required(login_url="/")
def turmas_forum(request, id):
    turma = Turma.objects.get(id=id)
    return render(request, 'turmas/turma_forum.html', {'turma': turma})

#Todas as Views de personalização da Turma
@login_required(login_url="/")
def criar_turma(request):
    form = TurmaForm(request.POST or None)
    teste = 3

    if form.is_valid():
        form.save()
        return redirect('turmas:list')
    return render(request, 'turmas/criar_turma.html', {'form': form, 'teste': teste})

@login_required(login_url="/")
def atualizar_turma(request, id):
    turma = Turma.objects.get(id=id)
    form = TurmaForm(request.POST or None, instance=turma)

    if form.is_valid():
        form.save()
        return redirect('turmas:detail', id=id)

    return render(request, 'turmas/criar_turma.html', {'form': form, 'turma': turma})

#Todas as Views de personalização de Aula
@login_required(login_url="/")
def criar_aula(request, id):
    turma = Turma.objects.get(id=id)
    form = AulaForm(request.POST or None, initial={'turma': turma})

    if form.is_valid():
        form.save()
        return redirect('turmas:aulas', id=id)

    return render(request, 'turmas/criar_aula.html', {'form': form, 'turma': turma})

@login_required(login_url="/")
def excluir_aula(request, id, id1):
    turma = Turma.objects.get(id=id)
    aula = Aula.objects.get(id=id1)

    if request.method == 'POST':
        aula.delete()
        return redirect('turmas:aulas', id=id)

    return render(request, 'turmas/aula_delete_confirm.html', {'turma': turma, 'aula': aula})

@login_required(login_url="/")
def atualizar_aula(request, id, id1):
    turma = Turma.objects.get(id=id)
    aula = Aula.objects.get(id=id1)
    form = AulaForm(request.POST or None, instance=aula)

    if form.is_valid():
        form.save()
        return redirect('turmas:aulas', id=id)

    return render(request, 'turmas/criar_aula.html', {'form': form, 'aula': aula, 'turma': turma})

@login_required(login_url="/")
def presenca_aula(request, id, id1):
    turma = Turma.objects.get(id=id)
    aula = Aula.objects.get(id=id1)

    form = PresencaForm(request.POST or None, instance=aula, turmaid=turma.id)

    if form.is_valid():
        form.save()
        return redirect('turmas:aulas', id=id)

    return render(request, 'turmas/presenca_aula.html', {'aula': aula, 'turma': turma, 'form': form})

@login_required(login_url="/")
def criar_nota(request, id):
    turma = Turma.objects.get(id=id)
    estudantes = turma.estudantes.all()
    for estudante in estudantes:
        for nota in estudante.nota_set.all():
            if nota.turma == turma:
                notaformset = modelformset_factory(Nota, form=NotaForm, extra=0)
                queryset = Nota.objects.filter(turma=turma)
                formset = notaformset(request.POST or None, queryset=queryset)

                if formset.is_valid():
                    formset.save()
                    return redirect('turmas:notas', id=id)
            else:
                notaformset = modelformset_factory(Nota, form=NotaForm, extra=len(estudantes))
                queryset = Nota.objects.filter(turma=turma)
                formset = notaformset(request.POST or None, queryset=queryset, initial=[{'turma': turma, 'aluno': estudante}
                                                                                        for estudante in estudantes])

                if formset.is_valid():
                    formset.save()
                    return redirect('turmas:notas', id=id)

    return render(request, 'turmas/criar_nota.html', {'turma': turma, 'formset': formset})

@login_required(login_url="/")
def add_estudantes(request, id):
    teste = 4
    turma = Turma.objects.get(id=id)
    form = AddEstudantesForm(request.POST or None, instance=turma)

    if form.is_valid():
        form.save()
        return redirect('turmas:alunos', id=id)

    return render(request, 'turmas/criar_turma.html', {'form': form, 'turma': turma, 'teste': teste})

@login_required(login_url="/")
def criar_postagem(request, id):
    turma = Turma.objects.get(id=id)
    form = PostagemForm(request.POST or None, initial={'turma': turma, 'user': request.user})

    if form.is_valid():
        form.save()
        return redirect('turmas:forum', id=id)
    return render(request, 'turmas/criar_postagem.html', {'form': form, 'turma': turma})

@login_required(login_url="/")
def atualizar_postagem(request, id, id1):
    turma = Turma.objects.get(id=id)
    postagem = Postagem.objects.get(id=id1)
    form = PostagemForm(request.POST or None, instance=postagem)

    if form.is_valid():
        form.save()
        return redirect('turmas:forum', id=id)

    return render(request, 'turmas/criar_postagem.html', {'form': form, 'postagem': postagem, 'turma': turma})

@login_required(login_url="/")
def excluir_postagem(request, id, id1):
    turma = Turma.objects.get(id=id)
    postagem = Postagem.objects.get(id=id1)

    if request.method == 'POST':
        postagem.delete()
        return redirect('turmas:forum', id=id)

    return render(request, 'turmas/postagem_delete_confirm.html', {'turma': turma, 'postagem': postagem})

@login_required(login_url="/")
def exibir_postagem(request, id, id1):
    turma = Turma.objects.get(id=id)
    postagem = Postagem.objects.get(id=id1)

    return render(request, 'turmas/forum_post.html', {'turma': turma, 'postagem': postagem})

@login_required(login_url="/")
def criar_resposta(request, id, id1):
    turma = Turma.objects.get(id=id)
    postagem = Postagem.objects.get(id=id1)
    form = RespostaForm(request.POST or None, initial={'postagem': postagem, 'user': request.user})

    if form.is_valid():
        form.save()
        return redirect('turmas:exibir_postagem', id=id, id1=id1)
    return render(request, 'turmas/criar_postagem.html', {'form': form, 'postagem': postagem, 'turma': turma})