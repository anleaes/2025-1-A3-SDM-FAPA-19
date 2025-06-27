from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.permissions import AllowAny
from pequenium_api.views import UserView, LogoutView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

from rest_framework.permissions import AllowAny
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token-autenticacao/', obtain_auth_token),
    path('deslogar/', LogoutView.as_view(), name='logout'),
    path('informacoes-de-usuario/', UserView.as_view(), name='user-info'),
    path('artigos/', include('newsarticle.urls', namespace='newsarticle')),
    path('categorias/', include('category.urls', namespace='category')),
    path('usuario/', include('user.urls', namespace='user')),
    path('tags/', include('tag.urls', namespace='tag')),
    path('listas-leitura/', include('readinglist.urls', namespace='readinglist')),
    path('itens-lista-leitura/', include('readinglistitem.urls', namespace='readinglistitem')),
    path('interacoes-usuario-artigo/', include('userarticleinteraction.urls', namespace='userarticleinteraction')),
    path('artigos-tags/', include('newsarticletag.urls', namespace='newsarticletag')),
    path('artigos-categorias/', include('newsarticlecategory.urls', namespace='newsarticlecategory')),
]

urlpatterns += router.urls

