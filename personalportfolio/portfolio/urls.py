# portfolio/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about_me, name='about_me'),
    path('view-cv/', views.view_cv, name='view_cv'),
    path('edit-cv/', views.edit_cv, name='edit_cv'),
    path('edit-cv/add/', views.add_cv_section, name='add_cv_section'),
    path('edit-cv/edit/<int:pk>/', views.edit_cv_section, name='edit_cv_section'),
    path('edit-cv/delete/<int:pk>/', views.delete_cv_section, name='delete_cv_section'),
    path('', views.about_me, name='home'), # Setează pagina About Me ca pagină de start
]