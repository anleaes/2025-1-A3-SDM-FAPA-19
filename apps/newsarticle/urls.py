from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework.permissions import AllowAny

app_name = 'newsarticle'

router = routers.DefaultRouter()
router.register('', views.UserNewsArticleViewSet, basename='newsarticle')

urlpatterns = [
    path('all/', views.PublicNewsArticleViewSet.as_view({'get': 'list'}), name='all-articles'),
    path('', include(router.urls)),
]