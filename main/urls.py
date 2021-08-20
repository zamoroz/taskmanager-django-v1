from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view.as_view(), name='home'),
    path('new_task/', views.task_view.as_view(), name='new_task'),
    path('task/<int:task_id>/', views.edit_task, name='task'), 
    path('task/delete_<int:task_id>/', views.delete_task, name='delete'),
    path('task/success_<int:task_id>/', views.success_task, name='success'),
    path('task/defeat_<int:task_id>/', views.defeat_task, name='defeat'),
    path('sign-up/', views.sign_up.as_view(), name='sign-up'),
    path('sign-in/', views.sign_in.as_view(), name='sign-in'),
    path('logout/', views.logout_user, name='logout'),
]