from django.urls import path
from .views import *

urlpatterns = [
    path('', sup_home, name='sup_homepage'),
    path('create_project/', createProject, name='create_project_page'),
    path('my_project_list',myProject, name="my_project_list_page")
    # path('register/', register, name='registerpage'),
]
