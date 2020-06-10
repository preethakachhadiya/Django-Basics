from django.urls import path,include
from django.contrib.auth import views as auth_views
from accounts import views as accounts_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('register/',accounts_views.register,name='register'),
    path('profile/', accounts_views.profile,name="profile")
]
