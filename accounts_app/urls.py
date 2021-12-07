from django.contrib.auth.views import LogoutView
from django.urls import path
from accounts_app.views import LoginView, RegisterView

app_name = 'auth'
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]
