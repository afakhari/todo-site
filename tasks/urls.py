from django.urls import path
from . import views
urlpatterns = [
    path('', views.tasks_list, name='tasks_list'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('create/', views.create_task, name='create_task'),
    path('task/<int:pk>/', views.TaskDetailView.as_view(), name='task_detail'),
]
