from django.shortcuts import render, redirect
from .models import Entry
from .form import EntryForm
from django.contrib.auth.decorators import login_required

@login_required(login_url="/")
def index(request):
    entries = Entry.objects.all().order_by('-date').reverse()
    return render(request, 'calendario/index.html', {'entries': entries})

@login_required(login_url="/")
def details(request, pk):
    entry = Entry.objects.get(id=pk)
    return render(request, 'calendario/details.html', {'entry': entry})

@login_required(login_url="/")
def add(request):

    if request.method == 'POST':
        form = EntryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('calendario:index')

    else:
        form = EntryForm()

    return render(request, 'calendario/form.html', {'form': form})

@login_required(login_url="/")
def delete(request, id):
    entry = Entry.objects.get(id=id)
    if request.method == 'POST':
        entry.delete()
        return redirect('calendario:index')
    return render(request, 'calendario/delete.html', {'entry': entry})

@login_required(login_url="/")
def alterar(request, id):
    entry = Entry.objects.get(id=id)

    form = EntryForm(request.POST or None, instance=entry)

    if form.is_valid():
        form.save()
        return redirect('calendario:index')

    return render(request, 'calendario/form.html', {'form': form})