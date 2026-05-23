from django.urls import path
from .views import task_list, delete_task, toggle_complete, edit_task

urlpatterns = [
    path('', task_list, name='task_list'),
    path(
        'delete/<int:task_id>/',
        delete_task,
        name='delete_task'
    ),
    path('complete/<int:task_id>/',
         toggle_complete,
         name='toggle_complete'
    ),
    path('edit/<int:task_id>/',
         edit_task,
         name='edit_task'
    ),
]