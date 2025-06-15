from django.urls import path
from . import views

urlpatterns = [

    path('', views.public_home, name='public_home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),


    path('dashboard/', views.Inicio, name='dashboard'),
    

    path('notes/new/', views.note_create, name='note_create'),
    path('notes/<int:pk>/edit/', views.note_update, name='note_update'),
    path('notes/<int:pk>/delete/', views.note_delete, name='note_delete'),


    path('files/upload/', views.file_upload, name='file_upload'),
    path('files/<int:pk>/delete/', views.file_delete, name='file_delete'),
]