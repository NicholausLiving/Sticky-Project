

from django.urls import path
from .views import NoteListCreate, NoteDetail

urlpatterns = [
    path('notes/', NoteListCreate.as_view(), name='note_list_create'),
    path('notes/<int:pk>/', NoteDetail.as_view(), name='note_detail'),
]
