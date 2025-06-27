from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('informacoes/', views.UserView.as_view(), name='user-info'),
    path('deslogar/', views.LogoutView.as_view(), name='logout'),
]