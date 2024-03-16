from django.urls import path
from operations import views


urlpatterns = [
    path('sign-in/', views.sign_in, name='sign-in'),
    path('sign-out/', views.sign_out, name='sign-out'),
    path('sign-up/', views.sign_up, name='sign-up'),

    path('', views.home, name='home'),
    path('create-task', views.create_task, name='create-task'),
    path('create-todo', views.create_todo, name='create-todo'),
    path('update-task/<str:pk>/', views.update_task, name='update-task'),
    path('update-todo/<str:pk>/', views.update_todo, name='update-todo'),
    path('delete-task/<str:pk>/', views.delete_task, name='delete-task'),
    path('delete-todo/<str:pk>/', views.delete_todo, name='delete-todo'),
    path('get-doughnut-data/', views.doughnut_plot, name='doughnut-data'),
    path('get-areachart-data/', views.areachart, name='areachart-data'),
]
