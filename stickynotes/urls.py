# stickynotes/urls.py

from django.urls import path, include
from django.contrib import admin
from . import views

app_name = 'stickynotes'  

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin interface URL
    path('api/', include('stickynotes.notes.urls')),  # Include URLs from 'notes' app
    path('', views.home, name='home'),  # Root URL for rendering index.html
]
