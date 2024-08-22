from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import custom_logout
urlpatterns = [
    path('profile/<str:username>/', views.profile_view, name='profile_view'),
    path('profile/edit/<str:username>/', views.edit_profile, name='edit_profile'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('register/', views.register, name='register'),
    path('logout/', custom_logout, name='custom_logout'),
    
    
]
