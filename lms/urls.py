from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('user_registration/', views.user_registration, name='user_registration'),
]
