from django.urls import path
from .views import init_view, project_info

urlpatterns = [
    path('init', init_view, name='init'),
    path('project-info', project_info, name='project-info')
]
