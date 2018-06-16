from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Estudante, Professor, Coodenador
from django.db import transaction

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

        labels = {
            'username':"Usuário",
            'first_name':"Nome",
            'last_name':"Sobrenome",
            'email':"Email",
            'password1':"Senha",
            'password2':"Confirmação de Senha"
        }

        help_texts = {
            'username':"Requeridos até 150 caracteres ou menos. Letras, dígitos e @/./+/-/_ apenas"
        }

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].label="Senha"
        self.fields['password1'].help_text = "<li>Sua senha não pode ser muito" \
                                             " parecida com suas outras informações pessoais.</li>" \
                                             "<li>Sua senha deve conter pelo menos 8 caracteres.</li>" \
                                             "<li>Sua senha não pode ser uma senha comumente usada.</li>" \
                                             "<li>Sua senha não pode ser totalmente numérica.</li>"
        self.fields['password2'].label="Confirmação de Senha"
        self.fields['password2'].help_text="Digite a mesma senha de antes, para verificação."

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name(self.cleaned_data['first_name'])
        user.last_name(self.cleaned_data['last_name'])
        user.email(self.cleaned_data['email'])

        if commit:
            user.save()

        return user



class EstudanteSignUpForm(UserCreationForm):
    matricula = forms.IntegerField()
    nome_mae = forms.CharField(max_length=100)
    data_nascimento = forms.DateField()
    ano_ingresso = forms.IntegerField()
    serie = forms.IntegerField()

    class Meta(UserCreationForm.Meta):
        model = User

        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

        labels = {
            'username': "Usuário",
            'first_name': "Nome",
            'last_name': "Sobrenome",
            'email': "Email",
            'password1': "Senha",
            'password2': "Confirmação de Senha"
        }

        help_texts = {
            'username': "Requeridos até 150 caracteres ou menos. Letras, dígitos e @/./+/-/_ apenas"
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].label="Senha"
        self.fields['password1'].help_text = "<li>Sua senha não pode ser muito" \
                                             " parecida com suas outras informações pessoais.</li>" \
                                             "<li>Sua senha deve conter pelo menos 8 caracteres.</li>" \
                                             "<li>Sua senha não pode ser uma senha comumente usada.</li>" \
                                             "<li>Sua senha não pode ser totalmente numérica.</li>"
        self.fields['password2'].label="Confirmação de Senha"
        self.fields['password2'].help_text="Digite a mesma senha de antes, para verificação."

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.save()
        user.profile.is_estudante = True
        estudante = Estudante.objects.create(user = user)
        estudante.matricula = self.cleaned_data.get('matricula')
        estudante.nome_mae = self.cleaned_data.get('nome_mae')
        estudante.data_nascimento = self.cleaned_data.get('data_nascimento')
        estudante.ano_ingresso = self.cleaned_data.get('ano_ingresso')
        estudante.serie = self.cleaned_data.get('serie')
        estudante.save()

        return user

class ProfessorSignUpForm(UserCreationForm):
    cpf = forms.IntegerField()
    data_nascimento = forms.DateField()
    telefone = forms.IntegerField()
    endereco = forms.CharField(max_length=100)
    formacao = forms.CharField(max_length=30)

    class Meta(UserCreationForm.Meta):
        model = User

        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

        labels = {
            'username': "Usuário",
            'first_name': "Nome",
            'last_name': "Sobrenome",
            'email': "Email",
            'password1': "Senha",
            'password2': "Confirmação de Senha"
        }

        help_texts = {
            'username': "Requeridos até 150 caracteres ou menos. Letras, dígitos e @/./+/-/_ apenas"
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].label="Senha"
        self.fields['password1'].help_text = "<li>Sua senha não pode ser muito" \
                                             " parecida com suas outras informações pessoais.</li>" \
                                             "<li>Sua senha deve conter pelo menos 8 caracteres.</li>" \
                                             "<li>Sua senha não pode ser uma senha comumente usada.</li>" \
                                             "<li>Sua senha não pode ser totalmente numérica.</li>"
        self.fields['password2'].label="Confirmação de Senha"
        self.fields['password2'].help_text="Digite a mesma senha de antes, para verificação."

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.save()
        user.profile.is_coordenador = True
        professor = Professor.objects.create(user = user)
        professor.cpf = self.cleaned_data.get('cpf')
        professor.data_nascimento = self.cleaned_data.get('data_nascimento')
        professor.endereco = self.cleaned_data.get('endereco')
        professor.formacao = self.cleaned_data.get('formacao')
        professor.save()

        return user

class CoordenadorSignUpForm(UserCreationForm):
    cpf = forms.IntegerField()
    data_nascimento = forms.DateField()
    telefone = forms.IntegerField()
    endereco = forms.CharField(max_length=100)
    formacao = forms.CharField(max_length=30)

    class Meta(UserCreationForm.Meta):
        model = User

        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

        labels = {
            'username': "Usuário",
            'first_name': "Nome",
            'last_name': "Sobrenome",
            'email': "Email",
            'password1': "Senha",
            'password2': "Confirmação de Senha"
        }

        help_texts = {
            'username': "Requeridos até 150 caracteres ou menos. Letras, dígitos e @/./+/-/_ apenas"
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].label="Senha"
        self.fields['password1'].help_text = "<li>Sua senha não pode ser muito" \
                                             " parecida com suas outras informações pessoais.</li>" \
                                             "<li>Sua senha deve conter pelo menos 8 caracteres.</li>" \
                                             "<li>Sua senha não pode ser uma senha comumente usada.</li>" \
                                             "<li>Sua senha não pode ser totalmente numérica.</li>"
        self.fields['password2'].label="Confirmação de Senha"
        self.fields['password2'].help_text="Digite a mesma senha de antes, para verificação."

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.save()
        user.profile.is_coordenador = True
        coordenador = Coodenador.objects.create(user = user)
        coordenador.cpf = self.cleaned_data.get('cpf')
        coordenador.data_nascimento = self.cleaned_data.get('data_nascimento')
        coordenador.endereco = self.cleaned_data.get('endereco')
        coordenador.formacao = self.cleaned_data.get('formacao')
        coordenador.save()

        return user