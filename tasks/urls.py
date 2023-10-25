from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import AddTaskView, TaskList, TaskDetailsView, EditTaskView, CompleteTaskView, DeleteTaskView, DeleteImageView, TaskListCreateAPIView, TaskImageListCreateAPIView
from rest_framework.routers import DefaultRouter
# from .views import TaskList, TaskDetailsView, EditTaskView, CompleteTaskView, DeleteTaskView, add_task
# from . import views



router = DefaultRouter()
router.register(r'tasks', TaskListCreateAPIView)
router.register(r'tasks-images', TaskImageListCreateAPIView)


urlpatterns = [
    path('api/', include(router.urls)),
    path('', TaskList.as_view(), name='tasklist'),
    path('tasks/<int:pk>/', TaskDetailsView.as_view(), name='task-details'),
    path('tasks/add/', AddTaskView.as_view(), name='add-task'),
    # path('tasks/add/', add_task, name='add-task'),
    path('tasks/<int:task_id>/complete/', CompleteTaskView.as_view(), name='complete-task'),
    path('tasks/<int:task_id>/edit/', EditTaskView.as_view(), name='edit-task'),
    path('tasks/<int:task_id>/delete/', DeleteTaskView.as_view(), name='delete-task'),
    # path('tasks/<int:task_id>/images/<int:image_id>/delete/', views.delete_image, name='delete-image'),
    path('tasks/<int:task_id>/images/<int:image_id>/delete/', DeleteImageView.as_view(), name='delete-image'),


    # path('api/tasks/', TaskListCreateAPIView.as_view(), name='api_task_list_create'),
    # path('api/tasks/<int:pk>/', TaskRetrieveUpdateDestroyAPIView.as_view(), name='api_task_detail'),

    
    # path('api/tasks/images/', TaskImageListCreateAPIView.as_view(), name='api_task_image_list_create'),
    # path('api/tasks/images/<int:pk>/', TaskImageRetrieveUpdateDestroyAPIView.as_view(), name='api_task_image_detail'),
    
]