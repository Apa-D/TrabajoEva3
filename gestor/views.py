from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Note, UploadedFile
from .forms import NoteForm, UploadedFileForm



def public_home(request):
    total_notes = Note.objects.count()
    total_files = UploadedFile.objects.count()
    return render(request, 'public_home.html', {'total_notes': total_notes, 'total_files': total_files})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('public_home')


@login_required
def Inicio(request):
    notes = Note.objects.filter(user=request.user)
    files = UploadedFile.objects.filter(user=request.user)
    return render(request, 'private/dashboard.html', {'notes': notes, 'files': files})


@login_required
def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user  
            note.save()
            return redirect('dashboard')
    else:
        form = NoteForm()
    return render(request, 'private/note_form.html', {'form': form, 'title': 'Crear Nota'})

@login_required
def note_update(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = NoteForm(instance=note)
    return render(request, 'private/note_form.html', {'form': form, 'title': 'Editar Nota'})

@login_required
def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    if request.method == 'POST':
        note.delete()
        return redirect('dashboard')
    return render(request, 'private/confirm_delete.html', {'object': note})



@login_required
def file_upload(request):
    if request.method == 'POST':
        form = UploadedFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.save(commit=False)
            uploaded_file.user = request.user
            uploaded_file.save()
            return redirect('dashboard')
    else:
        form = UploadedFileForm()
    return render(request, 'private/file_form.html', {'form': form})


@login_required
def file_delete(request, pk):
    file_to_delete = get_object_or_404(UploadedFile, pk=pk, user=request.user)
    if request.method == 'POST':
        file_to_delete.file.delete() 
        file_to_delete.delete() 
        return redirect('dashboard')
    return render(request, 'private/confirm_delete.html', {'object': file_to_delete})