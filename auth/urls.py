from .views import login, signup, logout, home, manage_employees, active, delete_user
from django.urls import path,include


urlpatterns = [
        path('signup', signup, name='signup'),
        path('login', login, name='login'),
        path('logout', logout, name='logout'),
        path('', home, name='home'),
        path('manage_employees', manage_employees, name='manage_employees'),
        path('active/<id>', active, name='active'),
        path('delete_user/<id>', delete_user, name='delete_user'),
        ]
