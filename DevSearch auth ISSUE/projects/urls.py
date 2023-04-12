from django.contrib import admin
from django.urls import path
from . import views


# Here all our urls paterns will be defined and corresrporndind defs to their views will be mapped...



urlpatterns = [
    
    path('',views.projects,name="projects"),
    path('project/<str:pk>',views.project,name="project"),    #define params here
    path('create-project/', views.createProject, name="create-project"),
    path('update-project/<str:pk>/', views.updateProject ,name="update-project"),
    path('delete-project/<str:pk>/', views.deleteProject ,name="delete-project"),
]