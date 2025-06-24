
# blog/urls.py

from django.urls import path
from . import views
from .views import logout_view

urlpatterns = [
    path('', views.home, name='home'),      # http://127.0.0.1:8000/
    path('dashboard/', views.dashboard, name='dashboard'),
    path('membros/', views.membros, name='membros'),
    path('logout/', logout_view, name='logout'),
     path('cadastro/', views.cadastro, name='cadastro'),
      path('edit/', views.edit, name='edit'),

]

