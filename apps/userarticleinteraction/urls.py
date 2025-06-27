from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'userarticleinteraction'

router = routers.DefaultRouter()
router.register('', views.UserArticleInteractionViewSet, basename='interacoes_usuario_artigo')

urlpatterns = [
    path('', include(router.urls) )
]