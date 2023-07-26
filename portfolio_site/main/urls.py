from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('post/<str:pk>/', views.post, name='post'),
    path('project/<str:pk>/', views.viewProject, name='project'),
    path('projects/', views.loadAllProjects, name='projects')
]
