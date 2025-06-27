from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'newsarticlecategory'

router = routers.DefaultRouter()
router.register('', views.NewsArticleCategoryViewSet, basename='artigos_categorias')

urlpatterns = [
    path('', include(router.urls) )
]