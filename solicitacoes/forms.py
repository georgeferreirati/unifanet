from django import forms
from turmas.models import Turma
from accounts.models import Estudante
from .models import Prova

class MatriculaForm(forms.ModelForm):
    class Meta:
        model = Estudante
        fields = {
            'turmas',
        }

    turmas = forms.ModelMultipleChoiceField(
                                    required=False, queryset=Turma.objects.all(),
                                    widget=forms.CheckboxSelectMultiple(attrs={'user.username': ("Add presenca")})
                                )

    def __init__(self, *args, **kwargs):
        if kwargs.get('instance'):
            initial = kwargs.setdefault('initial', {})
            initial['turmas'] = [t.pk for t in kwargs['instance'].turma_set.all()]

        forms.ModelForm.__init__(self, *args, **kwargs)

    def save(self, commit=True):
        instance = forms.ModelForm.save(self, False)

        old_save_m2m = self.save_m2m
        def save_m2m():
            old_save_m2m()
            instance.turma_set.clear()
            for turma in self.cleaned_data['turmas']:
                instance.turma_set.add(turma)
        self.save_m2m = save_m2m

        if commit:
            instance.save()
            self.save_m2m()
        return instance

class ProvaForm(forms.ModelForm):
    class Meta:
        model = Prova
        fields = {
            'professor',
            'turma',
            'bimestre',
            'arquivo',
        }