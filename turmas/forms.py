from django import forms
from .models import Turma, Aula, Nota, Postagem, Resposta
from accounts.models import Estudante

class TurmaForm(forms.ModelForm):
    class Meta:
        model = Turma
        fields = (
            'name',
            'description',
            'estudantes',
        )

class AulaForm(forms.ModelForm):
    class Meta:
        model = Aula
        fields = (
            'title',
            'description',
            'turma'
        )

class PresencaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        turmaid = kwargs.pop('turmaid')
        super(PresencaForm, self).__init__(*args, **kwargs)
        self.fields['presenca'] = forms.ModelMultipleChoiceField(
                                    required=False, queryset=Estudante.objects.filter(turma__id=turmaid),
                                    widget=forms.CheckboxSelectMultiple(attrs={'user.username': ("Add presenca")})
                                )

    class Meta:
        model = Aula
        fields = (
            'title',
            'description',
            'turma',
            'presenca',
        )
        widgets = {'title': forms.HiddenInput,
                   'description': forms.HiddenInput,
                   'turma': forms.HiddenInput,
                   }

class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = (
            'aluno',
            'turma',
            'nota1',
            'nota2',
            'nota3',
            'nota4',
        )

class AddEstudantesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddEstudantesForm, self).__init__(*args, **kwargs)
        self.fields['estudantes'] = forms.ModelMultipleChoiceField(
                                    required=False, queryset=Estudante.objects.all(),
                                    widget=forms.CheckboxSelectMultiple(attrs={'user.get_full_name': ("Add estudantes")})
                                    )

    class Meta:
        model = Turma
        fields = (
            'name',
            'description',
            'estudantes',
        )
        widgets = {'name': forms.HiddenInput,
                   'description': forms.HiddenInput,
                   }

class PostagemForm(forms.ModelForm):
    class Meta:
        model = Postagem
        fields = (
            'titulo',
            'descricao',
            'turma',
            'user'
        )

class RespostaForm(forms.ModelForm):
    class Meta:
        model = Resposta
        fields = (
            'postagem',
            'texto',
            'user'
        )