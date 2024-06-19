# stickynotes/views.py

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .notes.models import Note  # Adjust the import path to match your project structure

# Basic view to render index.html
def home(request):
    return render(request, 'index.html')

# View to list all notes
def note_list(request):
    notes = Note.objects.all()
    notes_list = [{"id": note.id, "title": note.title, "content": note.content, "created_at": note.created_at, "updated_at": note.updated_at} for note in notes]
    return JsonResponse(notes_list, safe=False)

# View to get the details of a specific note
def note_detail(request, id):
    note = get_object_or_404(Note, id=id)
    note_data = {"id": note.id, "title": note.title, "content": note.content, "created_at": note.created_at, "updated_at": note.updated_at}
    return JsonResponse(note_data)
