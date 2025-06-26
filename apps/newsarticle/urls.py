from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework.permissions import AllowAny

app_name = 'newsarticle'

router = routers.DefaultRouter()
router.register('', views.NewsArticleViewSet, basename='artigos')

urlpatterns = [
    path('', include(router.urls)),
]