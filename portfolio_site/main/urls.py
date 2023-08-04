from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('post/<str:pk>/', views.post, name='post'),
    path('posts/', views.loadAllPosts, name='posts'),
    path('project/<str:pk>/', views.viewProject, name='project'),
    path('projects/', views.loadAllProjects, name='projects'),
    path('about/', views.about, name='about')
]
