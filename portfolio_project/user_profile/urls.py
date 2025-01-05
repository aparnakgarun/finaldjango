# your_app_name/urls.py
from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('users/', views.user_list, name='user_list'),
    path('users/create/', views.user_create, name='user_create'),
    path('users/<int:pk>/', views.user_detail, name='user_detail'),
    path('users/<int:pk>/edit/', views.user_update, name='user_update'),
    path('users/<int:pk>/delete/', views.user_delete, name='user_delete'),
    path('profiles/', RedirectView.as_view(url='/users/')),

    # Portfolio URLs
    path('portfolios/', views.portfolio_list, name='portfolio_list'),
    path('portfolios/create/', views.portfolio_create, name='portfolio_create'),
    path('portfolios/<int:pk>/edit/', views.portfolio_update, name='portfolio_update'),
    path('portfolios/<int:pk>/delete/', views.portfolio_delete, name='portfolio_delete'),

    # Project URLs
    path('projects/', views.project_list, name='project_list'),
    path('projects/create/', views.project_create, name='project_create'),
    path('projects/<int:pk>/edit/', views.project_update, name='project_update'),
    path('projects/<int:pk>/delete/', views.project_delete, name='project_delete'),
]
