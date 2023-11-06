from django.urls import path
from .views import UserRegistration
from .import views
from django.contrib.auth import views as auth_views
from librarywedev import settings

app_name = 'users'

urlpatterns = [
    path('register', views.UserRegistration, name = "signup"),
    path('login', views.UserLogin, name = 'login'), 
    path('logout', auth_views.LogoutView.as_view(next_page = settings.LOGOUT_REDIRECT_URL), name = 'logout'),  
]

