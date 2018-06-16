from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import MatriculaForm, ProvaForm
from turmas.models import Turma
from accounts.models import Estudante
from .models import Prova
from django.contrib.auth.decorators import login_required
import datetime

from .utils import render_to_pdf
# Create your views here.

@login_required(login_url="/")
def home(request):
    return render(request, 'solicitacoes/home.html')

@login_required(login_url="/")
def generate_pdf(request):
    turmas = Turma.objects.all()
    data = {
        'full_name': request.user.get_full_name(),
        'matricula': request.user.estudante.matricula,
        'serie': request.user.estudante.serie,
        'data': datetime.date.today().strftime("%d-%m-%Y"),
        'turmas': turmas,
        'user': request.user,
    }
    pdf = render_to_pdf('solicitacoes/declaracao.html', data)
    return HttpResponse(pdf, content_type='application/pdf')

@login_required(login_url="/")
def matricula(request):
    estudantes = Estudante.objects.all()
    for estudante in estudantes:
        if estudante.user == request.user:
            form = MatriculaForm(request.POST or None, instance=estudante)

            if form.is_valid():
                form.save()
                return redirect('solicitacoes:home')

    return render(request, 'solicitacoes/matricula.html', {'form': form})

@login_required(login_url="/")
def matricular_aluno(request):
    teste = 4
    turmas = Turma.objects.all()

    return render(request, 'solicitacoes/matricular_aluno.html', {'turmas': turmas, 'teste': teste})

@login_required(login_url="/")
def boletim(request, id):
    turmas = Turma.objects.all()
    estudante = Estudante.objects.get(id=id)
    data = {
        'turmas': turmas,
        'estudante': estudante,
        'data': datetime.date.today().strftime("%d-%m-%Y"),
    }
    pdf = render_to_pdf('solicitacoes/boletim.html', data)
    return HttpResponse(pdf, content_type='application/pdf')

@login_required(login_url="/")
def solicitar_boletim(request):
    estudantes = Estudante.objects.all()
    teste = 5

    return render(request, 'solicitacoes/solicitar_boletim.html', {'estudantes': estudantes, 'teste': teste})

@login_required(login_url="/")
def submeter_provas(request):
    form = ProvaForm(request.POST or None, request.FILES or None)
    teste = 6

    if form.is_valid():
        form.save()
        return redirect('solicitacoes:submeter_prova')
    return render(request, 'solicitacoes/submeter_prova.html', {'form': form, 'teste': teste})

@login_required(login_url="/")
def listar_provas(request):
    provas = Prova.objects.all()
    teste = 7

    return render(request, 'solicitacoes/listar_provas.html', {'provas': provas, 'teste': teste})