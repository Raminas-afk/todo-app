from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('new_task', views.new_task, name="new-task"),
    path('delete_task/<int:task_id>', views.delete_task, name="delete-task"),
    path('complete_task/<int:task_id>', views.complete_task, name="complete-task"),
    path('task_detail/<int:task_id>', views.task_detail, name="task-detail"),
    path('edit_task/<int:task_id>', views.edit_task, name="edit-task"),
    path('task_archive', views.task_archive, name="task-archive"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
