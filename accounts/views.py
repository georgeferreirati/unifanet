from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .forms import RegistrationForm, EstudanteSignUpForm, ProfessorSignUpForm, CoordenadorSignUpForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/")
def signup_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            #loggin
            login(request, user)
            return redirect('turmas:list')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #loggin
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('accounts:login')

@login_required(login_url="/")
def estudante_signup_view(request):
    teste = 1
    if request.method == 'POST':
        form = EstudanteSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('turmas:list')
    else:
        form = EstudanteSignUpForm()
    return render(request, 'accounts/signup.html', {'form': form, 'teste': teste})

@login_required(login_url="/")
def professor_signup_view(request):
    teste = 2
    if request.method == 'POST':
        form = ProfessorSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('turmas:list')
    else:
        form = ProfessorSignUpForm()
    return render(request, 'accounts/signup.html', {'form': form, 'teste': teste})

@login_required(login_url="/")
def coordenador_signup_view(request):
    teste = 8
    if request.method == 'POST':
        form = CoordenadorSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('turmas:list')
    else:
        form = ProfessorSignUpForm()
    return render(request, 'accounts/signup.html', {'form': form, 'teste': teste})