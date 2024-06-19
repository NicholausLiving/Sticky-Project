# main_project/urls.py

from django.contrib import admin
from django.urls import path, include
from stickynotes import views

app_name = 'mypythonproject'  # 

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin interface URL
    path('api/', include('stickynotes.urls')),  # Include URLs from - 
    path('', views.home, name='home'),  # Root URL for rendering index.html
]
