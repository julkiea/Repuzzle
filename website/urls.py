from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name ='home'),
    path('register_user/', views.register_user, name = 'register_user'),
    path('login_user/', views.login_user, name = 'login_user'),
    path('logout_user/', views.logout_user, name = 'logout_user'),
    path('add_puzzle/', views.add_puzzle, name = 'add_puzzle'),
    path('puzzle_list/', views.puzzle_list, name='puzzle_list'),
    path('puzzle/<int:pk>', views.puzzle, name= 'puzzle'),
    path('update_info/', views.update_info, name = 'update_info'),
    path('update_password/', views.update_password, name='update_password'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('my_puzzle', views.my_puzzle, name='my_puzzle'),
    path('puzzle/<int:pk>/delete/', views.delete_puzzle, name='delete_puzzle'),
    path('filter_puzzles/', views.filter_puzzles, name = 'filter_puzzles'),
    path('puzzle/<int:pk>/edit/', views.edit_puzzle, name='edit_puzzle'),
    path('search/', views.search_puzzle, name='search'),
]