from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'tag'

router = routers.DefaultRouter()
router.register('', views.TagViewSet, basename='tags')

urlpatterns = [
    path('', include(router.urls) )
]
