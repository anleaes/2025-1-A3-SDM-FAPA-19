from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token-autenticacao/', obtain_auth_token),
    path('categorias/', include('category.urls', namespace='category')),
]
