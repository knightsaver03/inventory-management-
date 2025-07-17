
from django.urls import path
from . import views

urlpatterns = [
    path('', views.startup_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('adminLogin/', views.admin_login_view, name='adminLogin'),
    path('admin_dashboard/', views.admin_dashboard_view, name='admin_dashboard'),
    path('add_user/', views.add_user_view, name='add_user'),
    path('remove_user/', views.remove_user_view, name='remove_user'),
]
