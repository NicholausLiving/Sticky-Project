from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Note
from .serializers import NoteSerializer

class NoteListCreate(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allow read-only access to unauthenticated users

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user) 

class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allow read-only access to unauthenticated users

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)
