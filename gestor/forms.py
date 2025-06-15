from django import forms
from .models import Note, UploadedFile

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['titulo', 'content']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título de la nota'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escribe tu nota aquí...'}),
        }
        error_messages = {
            'title': {
                'required': "El título es obligatorio.",
            },
            'content': {
                'required': "El contenido no puede estar vacío.",
            },
        }

class UploadedFileForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['description', 'file']
        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Descripción del archivo'}),
            'file': forms.FileInput(attrs={'class': 'form-control'}),
        }
        error_messages = {
            'description': {
                'required': "La descripción es obligatoria.",
            },
            'file': {
                'required': "Debes seleccionar un archivo.",
            },
        }