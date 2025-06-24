from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),          # rota principal "/"
    path('sobre/', views.sobre, name='sobre'),  # rota "/sobre/"
]