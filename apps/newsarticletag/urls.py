from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'newsarticletag'

router = routers.DefaultRouter()
router.register('', views.NewsArticleTagViewSet, basename='artigos_tags')

urlpatterns = [
    path('', include(router.urls) )
]