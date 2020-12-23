from django.urls import path
from .import views
urlpatterns = [
    path('', views.apiOverview, name='api-Overview'),
    path('task-list/', views.tasklist, name='task-list'),
    path('task-detail/<int:id>/', views.taskDetail, name='task-detail'),
    path('task-create/', views.taskCreate, name='task-create'),
    path('task-update/<int:id>', views.taskUpdate, name='task-update'),
    path('task-delete/<int:id>', views.taskDelete, name='task-delete'),

]